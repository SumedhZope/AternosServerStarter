import json
import requests

p = requests.post("http://localhost:3000/api/start?wait=true")
print(p.content)