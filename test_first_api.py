import requests
class TestFirstAPI:
    def test_hello_call(self):
         base_url = "https://playground.learnqa.ru/api"
         name = "Olya"
         data= {'name': name}

         response = requests.get(f"{base_url}/hello", params=data)

         assert response.status_code == 200, "Wrong response code"

         response_dict = response.json()
         assert "answer" in response_dict, "There is no field 'answer' in response"

         expected_response_text = f"Hello, {name}"
         actual_response_text = response_dict["answer"]
         assert actual_response_text == expected_response_text, "Actual text in the response is not correct"