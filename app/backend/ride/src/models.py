from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Segment(BaseModel):
    distance: Optional[float] = None
    date: Optional[datetime] = None


class RideRequest(BaseModel):
    segments: List[Segment]