import uvicorn
from fastapi import FastAPI

from .Segments import RideRequest
from .Ride import Ride

app = FastAPI()

@app.post("/calculate_ride_price")
def calculate_ride_price(request: RideRequest):
    ride = Ride(segments=request.segments)
    price = ride.calculatePrice()
    return {"price": price}

if __name__ == "__main__":
    uvicorn.run("src.api:app", host="0.0.0.0", port=3000, reload=True)
