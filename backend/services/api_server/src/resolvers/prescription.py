from ariadne import MutationType
from db.connection import get_session

mutation = MutationType()

@mutation.field("uploadPrescription")
def resolve_upload_prescription(_, info, file):
    # Save file reference
    # Create DB entry
    return {"id": "<new_id>", "rawText": "", "parsedDrugs": []}

upload_prescription_resolver = mutation