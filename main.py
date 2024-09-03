import requests

base_url = "https://playground.learnqa.ru/api"

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post(f"{base_url}/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')
cookies = {'auth_cookie': cookie_value}

response2 = requests.post(f"{base_url}/check_auth_cookie", cookies=cookies)

print(response2.text)
