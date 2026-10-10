"""STEP-5 deterministic feature: Report import results and test.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    if not value.strip(): raise ValueError("empty input")
    return "verified:"+value[:80]
