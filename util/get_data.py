import requests
import json 


URL = "https://dashboard-pio.herokuapp.com/companies"

request = requests.get(URL).json()
data = request['response']
data_length = len(data)

company_names = []

for i in range(0, data_length):
    company_names.append(data[i]['name'])

db = {}
for i in range(0, data_length):
    company_name = company_names[i]

    db[company_name] = data[i]
    db[company_name].pop('name', None)
    

for key, value in db.items():
    print("Key: {}\nValue: {}\n\n".format(key, value))

with open('result.json', 'w') as fp:
    json.dump(db, fp)
