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
    # Public reference data only; this is not proof of personal mining or earnings.
    url = "https://api.braiins.com/v1/public/pool-stats"
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        return jsonify({"source": "Braiins public API", "data": response.json(), "disclaimer": "Public market/pool data only; not your account balance or earnings."})
    except requests.RequestException:
        return jsonify({"source": "unavailable", "error": "Market data is temporarily unavailable. Please try again later.", "disclaimer": "No mining or earnings are simulated."}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
