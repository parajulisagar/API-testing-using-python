import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"
response= requests.get(api_url)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())
