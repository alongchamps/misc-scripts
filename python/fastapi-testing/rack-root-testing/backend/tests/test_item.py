# invocation: pytest --import-mode prepend -c ./backend/tests/pytest.ini -v

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def testGettingItemThatDoesntExist():
    response = client.get("/items/2723987")
    assert response.status_code == 404

def testNewItem():
    response = client.post("/items/", json={"name": "hello","description": "world"})
    assert response.status_code == 200

def testGetNewlyCreatedItem():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.content.find(b"hello") > 0
    assert response.content.find(b"world") > 0

def testNewItem2():
    response = client.post("/items/", json={"name": "item2","description": "description2"})
    assert response.status_code == 200

# test that we get back a valid respond when asking for '/items/'
def testGetAllInventoryItems():
    response = client.get("/items/")
    assert response.status_code == 200

def testDeleteInventoryItem():
    response = client.delete("/items/1")
    assert response.status_code == 200

def testDeleteItemAgain():
    response = client.delete("/items/1")
    assert response.status_code == 404
