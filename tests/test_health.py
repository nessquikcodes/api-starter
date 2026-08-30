from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "app": "api-starter"}


def test_get_item_returns_item():
    resp = client.get("/items/7")
    assert resp.status_code == 200
    assert resp.json() == {"id": 7, "name": "widget"}
