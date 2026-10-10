"""Customer import API: parse, validate, normalize, upsert and report."""
import os
import tempfile
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.import_pipeline import parse_rows
from app.customer_validation import validate_rows
from app.customer_storage import save_customers

app = FastAPI(title="Customer Data Import & Validation Service")
DB_PATH = os.getenv("CUSTOMER_DB_PATH", os.path.join(tempfile.gettempdir(), "inkplain-customer-import.sqlite3"))

class ImportRequest(BaseModel):
    format: str = Field(pattern="^(csv|json)$")
    data: str = Field(min_length=1, max_length=1000000)

@app.post("/import")
def import_customers(request: ImportRequest):
    try:
        rows = parse_rows(request.format, request.data)
    except (ValueError, TypeError) as exc:
        raise HTTPException(status_code=422, detail="invalid customer data") from exc
    accepted, rejected = validate_rows(rows)
    saved = save_customers(accepted, DB_PATH)
    return {"total": len(rows), "accepted": saved, "rejected": len(rejected), "errors": rejected}


class LegacyRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)

@app.post("/process", deprecated=True)
def legacy_process(request: LegacyRequest):
    """Keep the original starter exercise endpoint without changing /import."""
    payload = ImportRequest(format="csv", data=request.message)
    report = import_customers(payload)
    return {"status": "accepted", **report}
