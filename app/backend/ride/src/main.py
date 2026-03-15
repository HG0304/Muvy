from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

# calculate ride price
@app.post("/calc")
def calculate_ride_price(body: list[dict]):
    result = 0
    for mov in body:
        try:
            mov["ds"] = datetime.fromisoformat(str(mov.get("ds")).replace("Z", "+00:00"))
        except Exception:
            mov["ds"] = None

        if mov.get("dist") is not None and isinstance(mov.get("dist"), (int, float)) and mov.get("dist") > 0:
            if mov.get("ds") is not None and isinstance(mov.get("ds"), datetime):
                # overnight
                if mov["ds"].hour >= 22 or mov["ds"].hour <= 6:
                    # not sunday
                    if mov["ds"].weekday() != 6:
                        result += mov["dist"] * 3.90
                    # sunday
                    else:
                        result += mov["dist"] * 5
                else:
                    # sunday
                    if mov["ds"].weekday() == 6:
                        result += mov["dist"] * 2.9
                    else:
                        result += mov["dist"] * 2.10
            else:
                return {"result": -2}
        else:
            return {"result": -1}

    if result < 10:
        result = 10

    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app", host="0.0.0.0", port=3000, reload=True)
