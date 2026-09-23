"""Serviço documental. Não executa decisões clínicas."""
import hmac
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
META = json.loads((ROOT / "package-info.json").read_text())

def make_server(host, port, token):
    if len(token) < 32:
        raise ValueError("Configure SERVICE_API_TOKEN com pelo menos 32 caracteres")
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
            given = self.headers.get("Authorization", "").encode()
            if not hmac.compare_digest(given, ("Bearer " + token).encode()):
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
                return self.reply(200, {"name": META["name"], "version": META["original_version"], "capabilities": ["read_instructions"], "clinical_engine": False})
            if self.path == "/v1/instructions":
                content = (ROOT / "plugin-original/skills/instructions/SKILL.md").read_text()
                return self.reply(200, {"name": META["name"], "instructions": content, "clinically_validated": False})
            self.reply(404, {"error": "not_found"})
        def do_POST(self):
            self.close_connection = True
            if self.authenticated():
                self.reply(501, {"error": "clinical_engine_not_implemented", "message": "Este serviço não processa casos clínicos nem gera prescrições."})
    return ThreadingHTTPServer((host, port), Handler)

if __name__ == "__main__":
    make_server("0.0.0.0", int(os.environ.get("PORT", "8080")), os.environ.get("SERVICE_API_TOKEN", "")).serve_forever()
