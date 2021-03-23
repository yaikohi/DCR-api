"""
This file processes the data from the dashboard-pio.herokuapp api to a more usable data structure.
One time usage suffices. 
It creates a new .json file with the data from the dashboard-pio.herokuapp api.
"""

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
    
for i in range(0, data_length):
    print(data[i]["logo"])


# Saves the company_data json to a db.json file 
# with open('db.json', 'w') as fp:
#     json.dump(db, fp)
