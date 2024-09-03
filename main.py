from json.decoder import JSONDecodeError
import requests

base_url = "https://playground.learnqa.ru/api"
payload = {"name": "User"}

response = requests.get(f"{base_url}/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not JSON format") 