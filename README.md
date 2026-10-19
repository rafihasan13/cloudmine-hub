# CloudMine Hub

Phone-friendly real-mining monitoring starter. This project does not mine cryptocurrency by itself and does not promise earnings. Real mining requires a verified provider/account and paid hardware or hashpower.

## Deploy website/API (phone-friendly)
1. Open Render and choose **New > Web Service**.
2. Connect `rafihasan13/cloudmine-hub`.
3. Runtime: Python; Build command: `pip install -r requirements.txt`; Start command: `gunicorn app:app`.
4. Deploy. The frontend is served at `/`; API health is `/api/health`.

## Android
The `android/` folder is a minimal Java WebView wrapper for the deployed site. Set the production URL in `MainActivity.java`, then build an APK using an Android cloud build service or Android IDE. A local APK is not included yet.

## Safety
- Dashboard values are market/reference data, not mined balance.
- Never store provider API secrets in the browser or GitHub.
- Do not add deposits, withdrawals, or user balances until provider integration and legal/security review are complete.
- Market endpoint availability/rate limits can change; verify with the provider before relying on it.
