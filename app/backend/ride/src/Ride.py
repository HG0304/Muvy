from datetime import datetime
from .Segments import Segment
from typing import List

class Ride:
    segments: List[Segment]
    OVERNIGHT_FARE = 3.90
    OVERNIGHT_SUNDAY_FARE = 5.00
    SUNDAY_FARE = 2.90
    DAY_FARE = 2.10
    MIN_PRICE = 10.00

    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def addSegment(self, distance: float, date: datetime):
        self.segments.append(Segment(distance=distance, date=date))

    def calculatePrice(self) -> float:
        price = 0
        for segment in self.segments:
            if segment.isOverNight() and not segment.isSunday():
                price += segment.distance * self.OVERNIGHT_FARE
            if segment.isOverNight() and segment.isSunday():
                price += segment.distance * self.OVERNIGHT_SUNDAY_FARE
            if not segment.isOverNight() and segment.isSunday():
                price += segment.distance * self.SUNDAY_FARE
            if not segment.isOverNight() and not segment.isSunday():
                price += segment.distance * self.DAY_FARE
        return self.MIN_PRICE if price < self.MIN_PRICE else price
