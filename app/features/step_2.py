"""STEP-2 deterministic feature: Validate parsed customer rows.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    import csv,io
    rows=list(csv.DictReader(io.StringIO(value)))
    return str(len(rows))+" rows received"
