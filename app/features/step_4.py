"""STEP-4 deterministic feature: Persist accepted customer records.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    import sqlite3
    with sqlite3.connect(":memory:") as db:
        db.execute("create table items(value text)")
        db.execute("insert into items values (?)",(value,))
        return "saved:"+str(db.execute("select count(*) from items").fetchone()[0])
