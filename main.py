import requests

base_url = "https://playground.learnqa.ru/api"

response = requests.post(f"{base_url}/something")
print(response.status_code)
print(response.text)

