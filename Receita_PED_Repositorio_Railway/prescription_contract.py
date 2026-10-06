"""Reserved integration contract; no clinical rules or activation flag."""
CONTRACT_VERSION = "receita-prescription/1"
PRESCRIPTION_PATH = "/v1/pediatric/prescription"

def capabilities():
    return {"contract_version": CONTRACT_VERSION, "endpoint": PRESCRIPTION_PATH,
            "available": False, "validated_regimes": [],
            "reason_code": "validated_prescription_dependency_unavailable"}

def unavailable():
    return {"contract_version": CONTRACT_VERSION, "status": "unavailable",
            "error": "validated_prescription_dependency_unavailable",
            "message": "Nenhum regime prescritivo validado disponível nesta integração.",
            "clinical_validated": False, "prescribing_authorization": False,
            "requires_human_review": True, "prescription": None,
            "regime_id": None, "audit": None}
