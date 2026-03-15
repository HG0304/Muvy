from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)


# calculate ride price
@app.post("/calc")
def calc():
    result = 0

    for mov in request.json:
        try:
            mov["ds"] = datetime.fromisoformat(str(mov.get("ds")).replace("Z", "+00:00"))
        except Exception:
            mov["ds"] = None

        if mov.get("dist") is not None and mov.get("dist") is not None and isinstance(mov.get("dist"), (int, float)) and mov.get("dist") > 0:
            if mov.get("ds") is not None and mov.get("ds") is not None and isinstance(mov.get("ds"), datetime):
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
                return jsonify({"result": -2})
        else:
            return jsonify({"result": -1})

    if result < 10:
        result = 10

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=3000)
