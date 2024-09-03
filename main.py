import requests

base_url = "https://playground.learnqa.ru/api"

payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post(f"{base_url}/get_auth_cookie", data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))

