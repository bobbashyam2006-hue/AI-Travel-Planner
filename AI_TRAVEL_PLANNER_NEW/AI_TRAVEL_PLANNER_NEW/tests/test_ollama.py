import requests

def test_ollama_server():
    response = requests.get('http://localhost:11434/api/tags', timeout=10)
    assert response.status_code == 200
