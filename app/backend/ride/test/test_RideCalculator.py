from datetime import datetime
from src.RideCalculator import *

class segment:
    def __init__(self, datetime: datetime):
        self.date = datetime

def test_isOverNight():
    # given
    segment1 = segment(datetime.strptime("2026-03-13T00:00:00", "%Y-%m-%dT%H:%M:%S"))
    segment2 = segment(datetime.strptime("2026-03-13T12:00:00", "%Y-%m-%dT%H:%M:%S"))

    # when
    result1 = isOverNight(segment1)
    result2 = isOverNight(segment2)

    # then
    assert result1 == True
    assert result2 == False

def test_isSunday():
    # given
    segment1 = segment(datetime.strptime("2026-05-03T12:00:00", "%Y-%m-%dT%H:%M:%S"))
    segment2 = segment(datetime.strptime("2026-05-01T12:00:00", "%Y-%m-%dT%H:%M:%S"))

    # when
    result1 = isSunday(segment1)
    result2 = isSunday(segment2)

    # then
    assert result1 == True
    assert result2 == False