import requests
import json
import time

API_URL = "http://127.0.0.1:5000/add-app"
JSON_FILE = "mock_apps.json"

def send_mock_data(app_data):
    print(f"[*] Sending: {app_data['app_name']} v{app_data['version']}")
    try:
        response = requests.post(API_URL, data=app_data)
        print("[+] Response:", response.status_code)
    except Exception as e:
        print("[!] Error:", e)

if __name__ == "__main__":
    print("[*] Task 4 - Sending mock app data from JSON...")

    try:
        with open(JSON_FILE, "r") as f:
            apps = json.load(f)

        for app in apps:
            send_mock_data(app)
            time.sleep(1)  # slight delay between requests

        print("[✓] All apps sent successfully.")

    except FileNotFoundError:
        print("[!] JSON file not found.")
    except json.JSONDecodeError:
        print("[!] Error decoding JSON.")
