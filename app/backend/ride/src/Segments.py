from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, model_validator

class Segment(BaseModel):
    distance: Optional[float] = None
    date: Optional[datetime] = None

    def isOverNight(self):
        dt = self.date
        return dt.hour < 6 or dt.hour >= 22

    def isSunday(self):
        dt = self.date
        return dt.weekday() == 6

    def isValidDistance(self):
        return (self.distance is not None
                and isinstance(self.distance, (int, float))
                and self.distance > 0)

    def isValidDate(self):
        return self.date is not None and isinstance(self.date, datetime)

    @model_validator(mode="after")
    def check_valid(self):
        if not self.isValidDistance():
            raise ValueError("Invalid distance: must be a positive number.")
        if not self.isValidDate():
            raise ValueError("Invalid date.")
        return self

class RideRequest(BaseModel):
    segments: List[Segment]