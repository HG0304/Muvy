import uvicorn
from fastapi import FastAPI

from src.RideCalculator import calculate
from src.models import RideRequest

app = FastAPI()

@app.post("/calculate_ride_price")
def calculate_ride_price(request: RideRequest):
    price = calculate(request.segments)
    return {"price": price}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=3000, reload=True)
