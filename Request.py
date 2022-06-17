from urllib import request
import requests
import json
url='https://dog-api.kinduff.com/api/facts/number=25'
response = requests.get(url) #Istalgan o'zgaruvchi

a_json=json.dumps(response.json(), indent=3)
a=json.loads(a_json)
for i in a['facts']:
    print(i, '\n') 