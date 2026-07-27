from fastapi import FastAPI
import json

app = FastAPI(
    title="Nerkh API",
    description="API نرخ قیمت‌ها",
    version="1.0.0"
)

# خواندن اطلاعات قیمت‌ها
def load_data():
    with open("nerkh_data.json", "r", encoding="utf-8") as file:
        return json.load(file)

# صفحه اصلی
@app.get("/")
def home():
    return {
        "api": "Nerkh API",
        "status": "active"
    }

# دریافت قیمت‌ها
@app.get("/prices")
def get_prices():
    data = load_data()

    return {
        "api": "Nerkh API",
        "dollar": data["prices"]["usd"]["price"],
        "bitcoin": data["prices"]["bitcoin"]["price"],
        "update_date": data["last_update"]
    }
