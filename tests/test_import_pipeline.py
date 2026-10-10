import json
import sqlite3
from fastapi.testclient import TestClient
from app.main import app
import app.main as api

def test_csv_with_rejections(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "DB_PATH", str(tmp_path / "customers.db"))
    client = TestClient(app)
    rows = "name,email\nAda,ADA@example.com\nDuplicate,ada@example.com\n,missing@example.com\n"
    response = client.post("/import", json={"format": "csv", "data": rows})
    assert response.status_code == 200
    assert response.json()["accepted"] == 1
    assert response.json()["rejected"] == 2
    with sqlite3.connect(api.DB_PATH) as conn:
        assert conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0] == 1

def test_json_upsert(tmp_path, monkeypatch):
    monkeypatch.setattr(api, "DB_PATH", str(tmp_path / "customers.db"))
    client = TestClient(app)
    for name in ("Ada", "Ada Lovelace"):
        response = client.post("/import", json={"format": "json", "data": json.dumps([{"name":name,"email":"ada@example.com"}])})
        assert response.status_code == 200
    with sqlite3.connect(api.DB_PATH) as conn:
        assert conn.execute("SELECT name FROM customers").fetchone()[0] == "Ada Lovelace"

def test_invalid_json():
    response = TestClient(app).post("/import", json={"format":"json","data":"not-json"})
    assert response.status_code == 422
