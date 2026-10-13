# STEP-5 — Report import results and test

Use `pip install -r requirements.txt && pytest -q`. Read the source from app/main.py into app/features/step_5.py. This is an offline teaching implementation, not a production service.

## Database (Entity) Relations
The source-backed SQLite `customers` table is kept unchanged in STEP-5. See `STEP-5.erd` and the main `.inkp` tab `STEP-5-ERD`. It has two columns: email TEXT PRIMARY KEY, name TEXT NOT NULL. Upserts update existing names by email. No FK relations or extra tables exist.
