from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Segment(BaseModel):
    distance: Optional[float] = None
    date: Optional[datetime] = None


class RideRequest(BaseModel):
    segments: List[Segment]


app = FastAPI()

@app.post("/calculate_ride_price")
def calculate_ride_price(request: RideRequest):
    price = 0
    for segment in request.segments:
        # validate distance
        if segment.distance is None or not isinstance(segment.distance, (int, float)) or segment.distance <= 0:
            return {"price": -1}

        # validate date
        if segment.date is None or not isinstance(segment.date, datetime):
            return {"price": -2}

        dt = segment.date

        # overnight
        if dt.hour >= 22 or dt.hour <= 6:
            # not sunday
            if dt.weekday() != 6:
                price += segment.distance * 3.90
            # sunday
            else:
                price += segment.distance * 5
        else:
            # sunday
            if dt.weekday() == 6:
                price += segment.distance * 2.9
            else:
                price += segment.distance * 2.10

    if price < 10:
        price = 10

    return {"price": price}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=3000, reload=True)
