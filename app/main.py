"""Typed HTTP door delegating to a cumulative synthetic teaching pipeline."""
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from app.features.step_2 import transform as action_2
from app.features.step_3 import transform as action_3
app=FastAPI(title="customer-data-import-validation-service")
class Request(BaseModel):
    message:str=Field(min_length=1,max_length=2000)
@app.post("/process")
def process(request:Request)->dict[str,str]:
    """Apply validated, deterministic transformations in the defined order."""
    try:
        value=request.message
        value=action_2(value)
        value=action_3(value)
        return {"status":"accepted","result":value}
    except ValueError as exc:
        raise HTTPException(status_code=422,detail=str(exc)) from exc

from app.import_pipeline import parse_rows
from app.customer_validation import validate_rows
class ImportRequest(BaseModel):
    format: str = Field(pattern="^(csv|json)$")
    data: str = Field(min_length=1, max_length=1000000)

@app.post("/import")
def import_customers(request:ImportRequest):
    try:
        rows=parse_rows(request.format,request.data)
    except (ValueError, TypeError) as exc:
        raise HTTPException(status_code=422,detail="invalid customer rows") from exc
    accepted,rejected=validate_rows(rows)
    return {"total":len(rows),"accepted":len(accepted),"rejected":len(rejected),"errors":rejected}
