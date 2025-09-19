from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_single():
    r = client.post("/predict", json={"text": "I love this!"})
    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"label", "score"}

def test_predict_batch():
    r = client.post("/predict_batch", json={"texts": ["good", "bad"]})
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list) and len(body) == 2
