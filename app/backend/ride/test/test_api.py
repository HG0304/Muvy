from fastapi.testclient import TestClient
import httpx

def test_calculate_a_day_ride_price():
    # given
    input_data = {
        "segments": [
            {"distance": 10, "date": "2026-03-13T08:00:00"}
        ]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    # assert
    assert response.status_code == 200
    assert response.json() == {"price": 21}