"""
This file further processes the data in db.json to retrieve a list of URL's in which the logo's of the companies can be found. 

"""


import json 


# GLOBAL VARIABLES
URL = "https://dashboard-pio.herokuapp.com"
DB = "../db.json"

# Loading and reading the data from the db.json file
data = json.load(open(DB))
data_length = len(data)


logos = []
# Iterating over the db and adding the logo adresses to the logos list
for _, value in data.items():
    logos.append(value['logo'])


logo_url_db = []
# Creating the links for the logos and storing them in the logo_url_db for DCR
for logo in logos:
    logo_url_db.append("{}{}".format(URL, logo))

# print(logo_url_db)

# Adding the URLS to the db.json: changing the original attribute to the full URL
for key in data:
    for i in range(0, len(logo_url_db)):
        data[key]['logo'] = logo_url_db[i]

with open('db_full_logo_urls.json', 'w') as fp:
    json.dump(data, fp)