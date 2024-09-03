import requests

base_url = "https://playground.learnqa.ru/api"

response = requests.post(f"{base_url}/get_500")
print(response.status_code)

