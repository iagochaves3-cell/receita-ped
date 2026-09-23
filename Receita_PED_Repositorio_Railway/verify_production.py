"""Opt-in production smoke test. Prints only check names and booleans."""
import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def main():
    host = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")
    if not re.fullmatch(r"[a-z0-9-]+\.up\.railway\.app", host):
        raise SystemExit("Missing Railway public domain")
    token = os.environ["SERVICE_API_TOKEN"]
    failures = 0
    def call(path, authenticated=True, payload=None):
        headers = {"Content-Type": "application/json"}
        if authenticated:
            headers["Authorization"] = "Bearer " + token
        request = Request("https://" + host + path, headers=headers,
                          data=json.dumps(payload).encode() if payload is not None else None)
        try:
            with build_opener(NoRedirect()).open(request, timeout=75) as response:
                return response.status, json.loads(response.read(2_000_000))
        except HTTPError as exc:
            return exc.code, {}
        except (URLError, OSError, ValueError):
            return 0, {}
    def check(name, passed):
        nonlocal failures
        failures += not passed
        print(json.dumps({"check": name, "passed": bool(passed)}), flush=True)
    check("public_health", call("/health", False)[0] == 200)
    check("authentication_required", call("/v1/instructions", False)[0] == 401)
    status, result = call("/v1/instructions")
    check("authenticated_instructions", status == 200 and len(result.get("instructions", "")) > 100)
    status, result = call("/v1/capabilities")
    check("nexo_configured", status == 200 and result.get("nexo_configured") is True)
    check("arbitrary_file_denied", call("/../package-info.json")[0] == 404)
    research = {"query": "pediatric fluid therapy", "deidentified": True, "limit": 2}
    status, result = call("/v1/evidence/search", payload=research)
    check("live_research_proxy", status == 200 and bool(result.get("sources")) and result.get("clinical_validated") is False)
    status, result = call("/v1/clinical/review", payload={
        "research": research, "patient_context": {"age_months": 48, "weight_kg": 16},
        "claims": [{"claim_id": "synthetic", "statement": "Applicability to children requires review."}]})
    check("review_contract", status == 200 and result.get("status") in {
        "review_unavailable", "insufficient_evidence", "review_draft"} and
        result.get("clinical_validated") is False and result.get("prescribing_authorization") is False)
    print(json.dumps({"failures": failures, "clinical_validation": False}), flush=True)
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
