from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()

    # Check the main keys
    assert data["status_code"] == 200
    assert data["detail"] == "ok"
    assert data["result"] == "working"

    #Check that the 'system' key exists
    assert "systems" in data