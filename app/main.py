"""customer data import validation service: FastAPI learning entry point.
ICS layer: door / composition root.
Why it exists: binds a typed request handler to an HTTP endpoint.
Without it: requests cannot reach the example service.
Step: added in step 1 (Accept customer data upload).
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="customer data import validation service")

class Request(BaseModel):
    """A synthetic message that can be validated without a provider."""
    message: str = Field(min_length=1, max_length=2000)

def handle_request(message: str) -> dict[str, str]:
    """Return an explicit local acknowledgement, not a fabricated AI result."""
    return {"status": "accepted", "message": message}

@app.post("/process")
def process(request: Request) -> dict[str, str]:
    """Enforce the request schema before passing to the handler."""
    return handle_request(request.message)

from app.import_pipeline import parse_rows
from fastapi import HTTPException
class CustomerUpload(BaseModel):
    format: str = Field(pattern="^(csv|json)$")
    data: str = Field(min_length=1)
@app.post("/import")
def import_customers(payload:CustomerUpload):
    try:
        rows=parse_rows(payload.format,payload.data)
    except (ValueError,TypeError):
        raise HTTPException(status_code=422,detail="invalid rows")
    return {"total":len(rows),"rows":rows}
