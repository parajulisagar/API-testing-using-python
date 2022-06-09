import json
import requests
print("first methdo to read json data using dumps function")
api_url = "https://jsonplaceholder.typicode.com/todos/12"
todo={"title":'post todo using dumps function'}
headers={"Content-Type":"application/json"}
response= requests.patch(api_url,data=json.dumps(todo),headers=headers)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())