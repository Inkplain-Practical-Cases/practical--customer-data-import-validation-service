"""STEP-3 deterministic feature: Normalize and deduplicate data.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    return ",".join(dict.fromkeys(v.strip().lower() for v in value.split(",") if v.strip()))
