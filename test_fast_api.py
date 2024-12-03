from fastapi.testclient import TestClient
from main import app


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/duki")
    assert response.status_code == 200
    assert response.json() == {
        "result": ["mauro ezequiel lombardo", "june", "duki", "argentine"]
    }
