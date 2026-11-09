
import pytest
from app.web import create_app
@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_message_normal(client):
    response = client.post("/moderate", json={"message": "Hello, this is a normal message."})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}

def test_message_spam(client):
    response = client.post("/moderate", json={"message": "This is a spam message."})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}

def test_message_empty(client):
    response = client.post("/moderate", json={"message": ""})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}

def test_message_invalid(client):
    response = client.post("/moderate", json={"message": 42})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}

def test_message_espaces(client):
    response=client.post("/moderate",json={"message":"  "})

    assert response.status_code==400
    assert response.get_json()=={"error":"Invalid message"}


def test_json_liste(client):
    response=client.post(
        "/moderate",
        json=["Bonjour","spam"]
    )
    assert response.status_code==400
    assert response.get_json()=={"error":"JSON object required"}