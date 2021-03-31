import requests
import json 
import pickle


API_URL = "https://dashboard-pio.herokuapp.com/companies"

request = requests.get(API_URL).json()
data = request['response']

f = open("db.pkl", "wb")

for company in data:
    pickle.dump(company, f)

f.close



# writeFile = open('db.json', 'w')
# writeFile.write(data)
# writeFile.close()