from src.main import app


def test_app():
    client = app.test_client()
    payload = [{
        "dist": 10,
        "ds": "2026-03-15T12:00:00",
    }]
    response = client.post('/calc', json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "result" in data