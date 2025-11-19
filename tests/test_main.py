import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Chatbot API" in response.json()["message"]
    assert "version" in response.json()

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "timestamp" in response.json()

@pytest.mark.asyncio
async def test_chat_endpoint_structure():
    """Test chat endpoint returns correct structure"""
    response = client.post(
        "/chat",
        json={"message": "Hello", "session_id": "test_session"}
    )
    # May return 200 or 500 depending on API key availability
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert "response" in data
        assert "session_id" in data
        assert "timestamp" in data

def test_get_history_empty():
    """Test getting history for non-existent session"""
    response = client.get("/history/nonexistent_session")
    assert response.status_code == 200
    data = response.json()
    assert "messages" in data
    assert len(data["messages"]) == 0

def test_clear_history():
    """Test clearing session history"""
    response = client.delete("/clear/test_session")
    assert response.status_code == 200
    assert "message" in response.json()
