import sqlite3

def save_customers(customers, db_path):
    with sqlite3.connect(db_path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS customers (email TEXT PRIMARY KEY, name TEXT NOT NULL)")
        for row in customers:
            db.execute(
                "INSERT INTO customers(email,name) VALUES (?,?) ON CONFLICT(email) DO UPDATE SET name=excluded.name",
                (row["email"], row["name"]),
            )
    return len(customers)
