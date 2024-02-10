import requests

endpoint = "http://localhost:8000/api/"

get_respons = requests.get(endpoint, params={'username': 'admin', 'password': '<PASSWORD>'},json={'username': 'admin', 'password': '<PASSWORD>'})
print(get_respons.json())
