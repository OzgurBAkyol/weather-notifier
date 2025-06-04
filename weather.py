import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")

def get_weather_forecast():
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={CITY}&appid={API_KEY}&units=metric&lang=tr"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        forecast_list = data["list"]

        # Sabah, öğle, akşam için boş listeler
        morning = []
        afternoon = []
        evening = []

        today = datetime.now().date()

        for entry in forecast_list:
            dt_txt = entry["dt_txt"]
            dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")

            if dt.date() != today:
                continue

            hour = dt.hour
            block = {
                "temp": entry["main"]["temp"],
                "feels_like": entry["main"]["feels_like"],
                "temp_min": entry["main"]["temp_min"],
                "temp_max": entry["main"]["temp_max"],
                "humidity": entry["main"]["humidity"],
                "wind": entry["wind"]["speed"],
                "visibility": entry.get("visibility", 10000) / 1000,  # km
                "desc": entry["weather"][0]["description"]
            }

            if 6 <= hour <= 11:
                morning.append(block)
            elif 12 <= hour <= 17:
                afternoon.append(block)
            elif 18 <= hour <= 23:
                evening.append(block)

        def summarize(blocks):
            if not blocks:
                return None
            def avg(field): return round(sum(b[field] for b in blocks) / len(blocks), 1)
            def min_val(field): return round(min(b[field] for b in blocks), 1)
            def max_val(field): return round(max(b[field] for b in blocks), 1)
            def mode_desc(): 
                descs = [b["desc"] for b in blocks]
                return max(set(descs), key=descs.count)

            return {
                "avg_temp": avg("temp"),
                "feels_like": avg("feels_like"),
                "temp_min": min_val("temp_min"),
                "temp_max": max_val("temp_max"),
                "humidity": avg("humidity"),
                "wind": avg("wind"),
                "visibility": avg("visibility"),
                "desc": mode_desc()
            }

        weather_info = {
            "city": CITY,
            "morning": summarize(morning),
            "afternoon": summarize(afternoon),
            "evening": summarize(evening),
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"[HATA] Forecast API isteği başarısız: {e}")
        return None
