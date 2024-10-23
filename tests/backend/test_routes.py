from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_read_item_not_found():
    response = client.get("/items/1")
    assert response.status_code == 404

def test_add_item():
    response = client.post("/items/", params={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_cross_list():
    item_data = {
        "item_id": 1,
        "name": "Test Item",
        "quantity": 10
    }
    response = client.post("/cross-list/", json=item_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Item cross-listed and inventory synchronized."
