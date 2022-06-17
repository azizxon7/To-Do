import json
# from fayl.json import *
# 1-vazifa
d = {}
for i in range(3):
    a=input('Fan nomi - ')
    b=input('Bahoyingiz - ')
    d[a] = b
d_js=json.dumps(d)
print(d_js)
filename = 'fayl.json'
with open(filename, 'w') as file:
    file.write(d_js)
# 2-vazifa
mx=-12345678
for i in range(3):
    a=input('Fan nomi - ')
    b=int(input('Bahoyingiz - '))
    if mx<b:
        mx=b
    print(mx)
