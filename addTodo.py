import json
import requests
print("first methdo to read json data using dumps function")
api_url = "https://jsonplaceholder.typicode.com/todos"
todo={"userID":1,"title":'post todo using dumps function',"completed": True}
headers={"Content-Type":"application/json"}
response= requests.post(api_url,data=json.dumps(todo),headers=headers)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())


print("\n")
print("*******************************************************************************************")
print("\n")
print("using json = todo for posting jason file in request")
todo={"userID":1,"title":'post using json keyword to parse in json ',"completed": False}
response= requests.post(api_url,json=todo)
print(response.status_code)
print(response.json())


