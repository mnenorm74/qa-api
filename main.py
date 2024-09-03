import requests

base_url = "https://playground.learnqa.ru/api"

headers = {"some header": "123"}
response = requests.get(f"{base_url}/show_all_headers")
print(response.text)
print(response.headers)

