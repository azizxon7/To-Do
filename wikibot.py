from urllib import response
import requests as rq
from pprint import pprint as print
api='f545d99067dbe282d23f49a1'
kurs1='USD'
kurs2='UZS'
url=f'https://v6.exchangerate-api.com/v6/f545d99067dbe282d23f49a1/pair/{kurs1}/{kurs2}'
response=rq.get(url)
print(response.status_code)
print(response.json())
kurs=response.json()['conversion_rate']
print(f'Bugungi kurs: {kurs1} = {kurs} {kurs2}')