from datetime import datetime
import pytest
from pydantic import ValidationError

from src.RideCalculator import calculate
from src.Segments import Segment

def test_ride_price_on_not_sundays_day():
    # given
    segments = [Segment(distance=10, date=datetime.strptime("2026-03-13T08:00:00", "%Y-%m-%dT%H:%M:%S"))]

    # when
    price = calculate(segments)

    # assert
    assert price == 21

def test_ride_price_on_not_sundays_night():
    # given
    segments = [Segment(distance=10, date=datetime.strptime("2026-03-13T23:00:00", "%Y-%m-%dT%H:%M:%S"))]
    
    # when
    price = calculate(segments)

    # assert
    assert price == 39

def test_ride_price_on_sundays_day():
    # given
    segments = [Segment(distance=10, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))]
    
    # when
    price = calculate(segments)

    # assert
    assert price == 29

def test_ride_price_on_sundays_night():
    # given
    segments = [Segment(distance=10, date=datetime.strptime("2026-03-15T23:00:00", "%Y-%m-%dT%H:%M:%S"))]

    # when
    price = calculate(segments)

    # assert
    assert price == 50

def test_invalid_distanceance():
    with pytest.raises(ValidationError):
        Segment(distance=-10, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))

def test_price_below_minimum():
    # given
    segments = [Segment(distance=1, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))]
    
    # when
    price = calculate(segments)

    # assert
    assert price == 10

def test_multiple_segments():
    # given
    segments = [
        Segment(distance=10, date=datetime.strptime("2026-03-13T08:00:00", "%Y-%m-%dT%H:%M:%S")),
        Segment(distance=5, date=datetime.strptime("2026-03-13T10:00:00", "%Y-%m-%dT%H:%M:%S"))
    ]

    # when
    price = calculate(segments)

    # assert
    assert price == 21 + 21/2