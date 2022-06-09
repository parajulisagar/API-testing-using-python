import json
import requests
print("first methdo to read json data using dumps function")
api_url = "https://jsonplaceholder.typicode.com/todos/11"
todo={"userID":1,"title":'putopetation on todo using json ',"completed": True}
response= requests.put(api_url,json=todo)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())