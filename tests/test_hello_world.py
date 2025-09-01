import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_world_endpoint():
    """Test that the hello world endpoint returns 'HelloWorld !'"""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "HelloDevin!"}

def test_hello_world_endpoint_content_type():
    """Test that the hello world endpoint returns JSON content type"""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

def test_hello_world_endpoint_structure():
    """Test that the response has the correct structure"""
    response = client.get("/hello")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "message" in data
    assert data["message"] == "HelloDevin!"
