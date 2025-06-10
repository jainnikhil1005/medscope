from fastapi import FastAPI, UploadFile, File
from ariadne import load_schema_from_path, make_executable_schema, gql
from ariadne.asgi import GraphQL
from db.connection import get_session
from resolvers.interaction import check_interaction_resolver
from resolvers.prescription import upload_prescription_resolver

# Load GraphQL schema
type_defs = gql(load_schema_from_path("schema.graphql"))

# Map resolvers
resolvers = [
    upload_prescription_resolver,
    check_interaction_resolver,
]

schema = make_executable_schema(type_defs, *resolvers)

app = FastAPI()
app.mount("/graphql", GraphQL(schema, debug=True))

@app.post("/upload_prescription")
async def upload_prescription(file: UploadFile = File(...)):
    contents = await file.read()
    # TODO: persist file, enqueue OCR job
    return {"success": True, "prescriptionId": "<new_id>"}