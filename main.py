import requests

base_url = "https://playground.learnqa.ru/api"

payload = {"name": "User"}
response = requests.get(base_url + "/hello", params=payload)
print(response.text)
print(response.status_code)