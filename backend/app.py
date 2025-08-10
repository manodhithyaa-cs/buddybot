from __future__ import annotations
import time
from typing import Any, Dict

import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

from config import Settings

settings = Settings()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": settings.allowed_origins}}, supports_credentials=True)

# In-memory reminder store for MVP
reminders: list[Dict[str, Any]] = []

@app.get("/health")
def health() -> Any:
    return jsonify({"status": "ok", "time": int(time.time())})


@app.post("/chat")
def chat() -> Any:
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify({"error": "message is required"}), 400

    # Placeholder until a real conversational model is integrated
    reply_text = f"BuddyBot: You said '{message}'"
    return jsonify({"reply": reply_text}), 200


@app.get("/feature/weather")
def weather() -> Any:
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"error": "city query param is required"}), 400
    if not settings.openweather_api_key:
        return jsonify({"error": "OPENWEATHER_API_KEY not set on the server"}), 500

    try:
        params = {"q": city, "appid": settings.openweather_api_key, "units": "metric"}
        resp = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params=params, timeout=10
        )
        resp.raise_for_status()
        w = resp.json()
        result = {
            "city": w.get("name", city),
            "description": (w.get("weather") or [{}])[0].get("description"),
            "temp_c": w.get("main", {}).get("temp"),
            "feels_like_c": w.get("main", {}).get("feels_like"),
            "humidity": w.get("main", {}).get("humidity"),
            "wind_mps": w.get("wind", {}).get("speed"),
        }
        return jsonify(result)
    except requests.HTTPError as http_err:
        status = http_err.response.status_code if http_err.response else 502
        return jsonify({"error": "Failed to fetch weather", "details": str(http_err)}), status
    except Exception as exc:  # noqa: BLE001 - simple MVP error handling
        return jsonify({"error": "Unexpected error", "details": str(exc)}), 500


@app.get("/feature/joke")
def joke() -> Any:
    try:
        resp = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=10)
        resp.raise_for_status()
        j = resp.json()
        return jsonify({"setup": j.get("setup"), "punchline": j.get("punchline")})
    except Exception as exc:  # noqa: BLE001 - simple MVP error handling
        return jsonify({"error": "Failed to fetch joke", "details": str(exc)}), 502


@app.post("/feature/reminder")
def reminder() -> Any:
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    if not text:
        return jsonify({"error": "text is required"}), 400
    delay_seconds = int(data.get("delay_seconds") or 0)
    reminder_item: Dict[str, Any] = {
        "id": len(reminders) + 1,
        "text": text,
        "delay_seconds": delay_seconds,
        "created_at": int(time.time()),
    }
    reminders.append(reminder_item)
    return jsonify({"message": "Reminder set", "reminder": reminder_item}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=settings.port, debug=True)


