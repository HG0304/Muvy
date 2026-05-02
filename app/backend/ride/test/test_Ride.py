from datetime import datetime
from pydantic import ValidationError
import pytest
from src.Ride import Ride
from src.Segments import Segment

def test_ride_price_on_not_sundays_day():
    ride = Ride(segments=[])
    ride.addSegment(distance=10, date=datetime.strptime("2026-03-13T08:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 21

def test_ride_price_on_not_sundays_night():
    ride = Ride(segments=[])
    ride.addSegment(distance=10, date=datetime.strptime("2026-03-13T23:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 39

def test_ride_price_on_sundays_day():
    ride = Ride(segments=[])
    ride.addSegment(distance=10, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 29

def test_ride_price_on_sundays_night():
    ride = Ride(segments=[])
    ride.addSegment(distance=10, date=datetime.strptime("2026-03-15T23:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 50

def test_invalid_distanceance():
    with pytest.raises(ValidationError):
        Segment(distance=-10, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))

def test_invalid_date():
    with pytest.raises(ValidationError):
        Segment(distance=10, date="invalid-date")

def test_price_below_minimum():
    ride = Ride(segments=[])
    ride.addSegment(distance=1, date=datetime.strptime("2026-03-15T08:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 10

def test_multiple_segments():
    ride = Ride(segments=[])
    ride.addSegment(distance=10, date=datetime.strptime("2026-03-13T08:00:00", "%Y-%m-%dT%H:%M:%S"))
    ride.addSegment(distance=5, date=datetime.strptime("2026-03-13T10:00:00", "%Y-%m-%dT%H:%M:%S"))
    assert ride.calculatePrice() == 21 + 21/2