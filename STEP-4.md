# STEP-4 — Persist accepted customer records

Use `pip install -r requirements.txt && pytest -q`. Read the source from app/main.py into app/features/step_4.py. This is an offline teaching implementation, not a production service.

## Database (Entity) Relations
The source-backed SQLite `customers` table is introduced in STEP-4. See `STEP-4.erd` and the main `.inkp` tab `STEP-4-ERD`. It has two columns: email TEXT PRIMARY KEY, name TEXT NOT NULL. Upserts update existing names by email. No FK relations or extra tables exist.
