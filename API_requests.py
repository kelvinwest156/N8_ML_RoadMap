import  json
import requests

# get request
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# convert response to python
data = response.json()

with open("posts.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data saved.")
