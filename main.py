import requests

base_url = "https://playground.learnqa.ru/api"

response = requests.post(f"{base_url}/get_301", allow_redirects=False)
print(response.status_code)

