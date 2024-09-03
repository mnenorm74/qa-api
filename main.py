import requests

base_url = "https://playground.learnqa.ru/api"

response = requests.get(base_url + "/hello")
print(response.text)