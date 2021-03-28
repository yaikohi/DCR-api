"""
This file processes the data from the dashboard-pio.herokuapp api to a more usable data structure.
One time usage suffices. 
It creates a new .json file with the data from the dashboard-pio.herokuapp api.
"""

import requests
import json 


API_URL = "https://dashboard-pio.herokuapp.com/companies"

request = requests.get(API_URL).json()
data = request['response']
data_length = len(data)

company_names = []

# Original code is commented out below
def create_json_from_api(API_URL: str, FILENAME: str, DIR: str) -> json:
    request = requests.get(API_URL).json()
    data = request['response']
    data_length = len(data)

    # Creates a list of company names.
    for i in range(0, data_length):
        company_names.append(data[i]['name'])

    new_db = {}

    # Changes the structure of the json_db for new_db
    for i in range(0, data_length):
        # Name of a company
        company_name = company_names[i]

        # Appends the data of the company to the respective name
        new_db[company_name] = data[i]

        # Removes the 'name' attribute from the company.
        new_db[company_name].pop('name', None)

    # Saves the json file with the new json structure.    
    with open(FILENAME, 'w') as fp:
        json.dump(db, fp)


def fix_logo_url(URL_TO_ADD: str, JSON_DB: str, FILENAME: str):
    data = json.load(open(JSON_DB))
    data_length = len(data)

    for _, value in data.items():
        value['logo'] = str(URL_TO_ADD + value['logo'])
    
    with open(FILENAME, as 'w') as fp:
        json.dump(data, fp)


# Running the functions.
create_json_from_api(API_URL="https://dashboard-pio.herokuapp.com/companies", FILENAME="db_v1.json")
fix_logo_url(URL_TO_ADD="https://dashboard-pio.herokuapp.com", JSON_DB="db_v1.json", FILENAME="db_v2.json")


# !: Original code
# for i in range(0, data_length):
#     company_names.append(data[i]['name'])
# new_db = {}
# for i in range(0, data_length):
#     company_name = company_names[i]
#     new_db[company_name] = data[i]
#     new_db[company_name].pop('name', None)
# for i in range(0, data_length):
#     print(data[i]["logo"])
# Saves the company_data json to a db.json file 
# with open('db.json', 'w') as fp:
#     json.dump(db, fp)


"""
This part further processes the data in db.json to retrieve a list of URL's in which the logo's of the companies can be found. 

"""


# # GLOBAL VARIABLES
# URL_TO_ADD = "https://dashboard-pio.herokuapp.com"
# DB = "db.json"

# # Loading and reading the data from the db.json file
# data = json.load(open(DB))
# data_length = len(data)


# # Iterating over the db and adding the logo adresses to the logos list
# for _, value in data.items():
#     value['logo'] = str(URL_TO_ADD + value['logo'])


# # Saving the new dictionary to a new json file: db_full_logo_urls.json
# with open('db_full_logo_urls.json', 'w') as fp:
#     json.dump(data, fp)