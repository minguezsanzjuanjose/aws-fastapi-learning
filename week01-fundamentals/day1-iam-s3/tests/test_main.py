import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns correct info"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to FastAPI AWS Learning API"
    assert data["version"] == "1.0.0"
    assert "endpoints" in data
    assert "health" in data["endpoints"]


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_docs_endpoint_exists():
    """Test that the docs endpoint is available"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_json_exists():
    """Test that the OpenAPI JSON schema is available"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["info"]["title"] == "FastAPI AWS Learning"
    assert data["info"]["version"] == "1.0.0"
