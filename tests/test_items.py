import pytest
from fastapi.testclient import TestClient

from app import store
from app.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_store():
    store.reset()
    yield
    store.reset()


def test_create_item_returns_201_with_assigned_id():
    resp = client.post("/items", json={"name": "widget"})
    assert resp.status_code == 201
    assert resp.json() == {"id": 1, "name": "widget"}


def test_create_item_rejects_invalid_body():
    resp = client.post("/items", json={})
    assert resp.status_code == 422


def test_list_items_returns_created_items():
    client.post("/items", json={"name": "widget"})
    client.post("/items", json={"name": "gadget"})
    resp = client.get("/items")
    assert resp.status_code == 200
    assert resp.json() == [
        {"id": 1, "name": "widget"},
        {"id": 2, "name": "gadget"},
    ]


def test_get_item_returns_item():
    client.post("/items", json={"name": "widget"})
    resp = client.get("/items/1")
    assert resp.status_code == 200
    assert resp.json() == {"id": 1, "name": "widget"}


def test_get_missing_item_returns_404():
    resp = client.get("/items/999")
    assert resp.status_code == 404


def test_delete_item_removes_it():
    client.post("/items", json={"name": "widget"})
    resp = client.delete("/items/1")
    assert resp.status_code == 204
    assert client.get("/items/1").status_code == 404


def test_delete_missing_item_returns_404():
    resp = client.delete("/items/999")
    assert resp.status_code == 404
