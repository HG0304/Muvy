from src.main import app
from fastapi.testclient import TestClient
import httpx

def test_ride_price_on_not_sundays_day():
    # given
    input_data = [{
        "dist": 10,
        "ds": "2026-03-13T08:00:00"
        }]

    # when
    response = httpx.post("http://localhost:3000/calc", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["result"] == 21

def test_ride_price_on_not_sundays_night():
    # given
    input_data = [{
        "dist": 10,
        "ds": "2026-03-13T23:00:00"
        }]

    # when
    response = httpx.post("http://localhost:3000/calc", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["result"] == 39

def test_ride_price_on_sundays_day():
    # given
    input_data = [{
        "dist": 10,
        "ds": "2026-03-15T08:00:00"
        }]

    # when
    response = httpx.post("http://localhost:3000/calc", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["result"] == 29

def test_ride_price_on_sundays_night():
    # given
    input_data = [{
        "dist": 10,
        "ds": "2026-03-15T23:00:00"
        }]

    # when
    response = httpx.post("http://localhost:3000/calc", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["result"] == 50