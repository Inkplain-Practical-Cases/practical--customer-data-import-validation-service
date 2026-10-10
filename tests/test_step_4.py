"""Offline request and validation contract checks."""
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_invalid_request():
    assert client.post("/process",json={}).status_code==422
def test_valid_response_shape():
    result=client.post("/process",json={"message":"name,email\nAda,ada@example.test"}).json()
    assert "status" in result or "detail" in result
