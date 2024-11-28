import requests
import json

url = "http://localhost:9200/infra-logs"
headers = {"Content-Type": "application/json"}

with open("index_creation.json", "r") as f:
    index_config = json.load(f)

response = requests.put(url, headers=headers, json=index_config)
print(response.json())
