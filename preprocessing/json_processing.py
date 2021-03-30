import json

DB_data = json.load(open("./data/db_full_logo_urls.json"))

colors = {"primary" : "red",
"secondary" : "blue",
"tertiary" : "white"}

def add_colors_to_logo(JSON_DB: json):
    """
    Adds color attributes to the logo key in the company json database
    
    input: JSON_DB(json)
    output: .json file
    """
    colors = {"primary" : "red", "secondary" : "blue", "tertiary" : "white"}
    for company in JSON_DB:
        company_logo_url = JSON_DB[company]['logo']
        
        logo = {"url" : company_logo_url, "colors" : colors}

        JSON_DB[company]['logo'] = logo
    with open('company_db.json', 'w') as fp:
        json.dump(JSON_DB, fp)

add_colors_to_logo(DB_data)


