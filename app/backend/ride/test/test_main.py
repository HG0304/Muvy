from src.main import app
from fastapi.testclient import TestClient
import httpx

def test_ride_price_on_not_sundays_day():
    # given
    input_data = {
        "segments": [{
            "distance": 10,
            "date": "2026-03-13T08:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == 21

def test_ride_price_on_not_sundays_night():
    # given
    input_data = {
        "segments": [{
            "distance": 10,
            "date": "2026-03-13T23:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == 39

def test_ride_price_on_sundays_day():
    # given
    input_data = {
        "segments": [{
            "distance": 10,
            "date": "2026-03-15T08:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == 29

def test_ride_price_on_sundays_night():
    # given
    input_data = {
        "segments": [{
            "distance": 10,
            "date": "2026-03-15T23:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == 50

def test_invalid_distanceance():
    # given
    input_data = {
        "segments": [{
            "distance": -10,
            "date": "2026-03-15T08:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == -1

def test_price_below_minimum():
    # given
    input_data = {
        "segments": [{
            "distance": 1,
            "date": "2026-03-15T08:00:00"
        }]
    }

    # when
    response = httpx.post("http://localhost:3000/calculate_ride_price", json=input_data, timeout=5)
    output = response.json()

    print(output)

    # assert
    assert response.status_code == 200
    assert output["price"] == 10