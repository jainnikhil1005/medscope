from ariadne import MutationType
from db.connection import get_session

mutation = MutationType()

@mutation.field("checkInteraction")
def resolve_check_interaction(_, info, p1, p2):
    # Call parser_service to retrieve parsed drugs
    # Call interaction lookup
    # Persist result in DB
    status = "Safe"
    details = ""
    # TODO: implement orchestration logic
    return {"prescription1Id": p1, "prescription2Id": p2, "status": status, "details": details}

check_interaction_resolver = mutation