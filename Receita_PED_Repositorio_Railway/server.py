"""Serviço documental. Não executa decisões clínicas."""
import hmac
import json
import os
import re
from threading import BoundedSemaphore
from nexo_client import AdapterError, PATHS, MAX_BODY_BYTES, configured, forward
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
META = json.loads((ROOT / "package-info.json").read_text())

DOMAIN = 'prescription'

def make_server(host, port, token):
    if not re.fullmatch(r"[A-Za-z0-9_-]{32,256}", token):
        raise ValueError("Configure SERVICE_API_TOKEN com pelo menos 32 caracteres")
    slots = BoundedSemaphore(4)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass  # Não registra URLs, cabeçalhos, tokens ou conteúdo clínico.
        def reply(self, status, data):
            body = json.dumps(data, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)
        def authenticated(self):
            values = self.headers.get_all("Authorization", [])
            given = values[0].encode() if len(values) == 1 else b""
            scheme, separator, supplied = given.partition(b" ")
            if not (separator and scheme.lower() == b"bearer" and hmac.compare_digest(supplied, token.encode())):
                self.reply(401, {"error": "unauthorized"})
                return False
            return True
        def do_GET(self):
            if self.path == "/health":
                return self.reply(200, {"status": "ok", "clinical_engine": False})
            if self.path == "/":
                return self.reply(200, {"name": META["name"], "mode": "documentary", "clinical_engine": False})
            if not self.authenticated():
                return
            if self.path == "/v1/capabilities":
                return self.reply(200, {"name": META["name"], "version": META["original_version"], "capabilities": ["read_instructions", "evidence_search_proxy", "evidence_review_draft_proxy"], "nexo_configured": configured(), "domain": DOMAIN, "clinical_engine": False, "clinical_validation": False, "sites_integration_verified": False})
            if self.path == "/v1/instructions":
                content = (ROOT / "plugin-original/skills/instructions/SKILL.md").read_text()
                return self.reply(200, {"name": META["name"], "instructions": content, "clinically_validated": False})
            self.reply(404, {"error": "not_found"})
        def do_POST(self):
            self.close_connection = True
            if not self.authenticated():
                return
            if self.path not in PATHS:
                return self.reply(501, {"error": "clinical_engine_not_implemented", "message": "Geração de conduta/prescrição não implementada."})
            if self.headers.get("Transfer-Encoding"):
                return self.reply(400, {"error": "chunked_not_supported"})
            lengths = self.headers.get_all("Content-Length", [])
            if len(lengths) != 1 or not re.fullmatch(r"[0-9]+", lengths[0]):
                return self.reply(411, {"error": "content_length_required"})
            length = int(lengths[0])
            if length > MAX_BODY_BYTES:
                return self.reply(413, {"error": "body_too_large"})
            if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
                return self.reply(415, {"error": "json_required"})
            if not slots.acquire(blocking=False):
                return self.reply(429, {"error": "capacity_exceeded"})
            try:
                self.connection.settimeout(10)
                raw = self.rfile.read(length)
                if len(raw) != length:
                    return self.reply(400, {"error": "incomplete_body"})
                payload = json.loads(raw)
                result = forward(self.path, payload, DOMAIN)
                return self.reply(200, result)
            except (ValueError, UnicodeError):
                return self.reply(422, {"error": "invalid_json"})
            except TimeoutError:
                return self.reply(408, {"error": "request_timeout"})
            except AdapterError as exc:
                return self.reply(exc.status, {"error": exc.code, "clinical_validated": False})
            finally:
                slots.release()
    return ThreadingHTTPServer((host, port), Handler)

if __name__ == "__main__":
    make_server("0.0.0.0", int(os.environ.get("PORT", "8080")), os.environ.get("SERVICE_API_TOKEN", "")).serve_forever()
