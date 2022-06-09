import requests

api_url = "https://jsonplaceholder.typicode.com/todos/"
val = input("Enter TODO ID: ")
api_url+=val
response= requests.get(api_url)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())
print()