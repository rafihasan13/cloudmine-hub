import os
import requests
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="web", static_url_path="")

@app.get("/")
def home():
    return send_from_directory("web", "index.html")

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "app": "CloudMine Hub", "mode": "monitoring-demo"})

@app.get("/api/market")
def market():
    # Public BTC price reference only. It is not mining pool data or personal earnings.
    url = "https://api.coingecko.com/api/v3/simple/price"
    try:
        response = requests.get(
            url,
            params={"ids": "bitcoin", "vs_currencies": "usd", "include_24hr_change": "true"},
            headers={"accept": "application/json", "user-agent": "CloudMineHub/1.0"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        bitcoin = data.get("bitcoin")
        if not isinstance(bitcoin, dict) or "usd" not in bitcoin:
            raise ValueError("Unexpected market data response")
        return jsonify({
            "source": "CoinGecko public price API",
            "data": {
                "bitcoin_usd": bitcoin.get("usd"),
                "bitcoin_24h_change_percent": bitcoin.get("usd_24h_change"),
            },
            "disclaimer": "Public BTC price reference only; not mining pool data, a personal balance, or earnings."
        })
    except (requests.RequestException, ValueError):
        return jsonify({
            "source": "unavailable",
            "error": "Market data is temporarily unavailable. Please try again later.",
            "disclaimer": "No mining or earnings are simulated."
        }), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
