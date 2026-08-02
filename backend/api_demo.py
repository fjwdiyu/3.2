import requests

resp = requests.get("https://api.ipify.org?format=json", timeout=10)
resp.raise_for_status()
print(resp.json())
