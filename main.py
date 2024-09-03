import requests

base_url = "https://playground.learnqa.ru/api"
payload = {"param1": "value1"}

response = requests.post(f"{base_url}/check_type", data=payload)
print(response.status_code)

