import requests

base_url = "https://playground.learnqa.ru/api"
payload = {"name": "User"}

response = requests.get(f"{base_url}/hello", params=payload)
parsed_response_text = response.json()
print(parsed_response_text['answer'])