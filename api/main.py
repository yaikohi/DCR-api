from fastapi import FastAPI, HTTPException
import requests 

# ? Pylance underlines this import with a warning but it compiles fine. ( "Import 'dcr' could not be resolved - PylancereportMissingImports" )
from dcr import get_dominant_color


# Description for the docs page. ( http://127.0.0.1:8000/docs )
tags_metadata = [
    {
        "name": "Logos",
        "description": "The logos of the companies.",
    },
    {
        "name": "Companies",
        "description": "All the information of the companies."
    }
]


# TODO: Write schemas for in- and output responses.
app = FastAPI(
    title="DCR-api",
    description="For pioDash CMS.",
    version="0.1",
    openapi_tags=tags_metadata
)


# ! LOADING DATA FROM THE DATABASE
# Fetches the data from the database and constructs a local memory cache for queries.
# TODO: Double check the variable names for readability.
# TODO: Possible restrucuring of code.
db = requests.get("https://dashboard-pio.herokuapp.com/companies").json()['response']
url_first_half = "https://dashboard-pio.herokuapp.com"

# Lists to be filled with logo-urls and company-names.
list_of_companies = []
list_of_logo_urls = []


# looping over the dashboard-pio database
for i in range(len(db)):
    
    # Filling the list_of_company_names with company_names
    company_name = db[i]['name']
    if company_name in list_of_companies:
        pass
    else:
        list_of_companies.append(company_name)
    
    # Filling the list_of_logo_urls with logo_urls
    url = db[i]['logo']
    if url in list_of_logo_urls:
        pass
    else: 
        list_of_logo_urls.append(url_first_half+url)

# Dict that stores all the logo-urls of every company. (company_name = key, logo_url = value)
logos_dict = dict(zip(list_of_companies, list_of_logo_urls))



# ! API ROUTES
# Returns the full database.
@app.get("/", tags=["Companies"])
async def get_logos():
    return db


# TODO: Add a spelling check algorithm for the company names so that it corrects typos to the corresponding company name. This will make it more user-friendly.
# Returns the logo dict of a company specified in the url.
@app.get("/{company_name}", tags=["Logos"])
async def get_logo_colors(company_name: str) -> dict:

    # Raises an error when a typo occurs or the name is not in the database.    
    if company_name not in list_of_companies:
        raise HTTPException(status_code=404, 
        detail="404: Company not found. Mind case-sensitivity and use of spaces.")
    for i in range(len(db)):
        if company_name == db[i]['name']:
            return db[i]


# TODO: Add a way of checking the code runtime. Return the time data in the get request?
# TODO: Add a spelling check algorithm for the company names so that it corrects typos to the corresponding company name. This will make it more user-friendly.
# Returns the list of colors when the request body contains an url to the company logo.
@app.get("/{company_name}/colors", tags=["Logos"])
async def return_logo_colors(company_name: str) -> list:

    # Raises an error when a typo occurs or the name is not in the database.    
    if company_name not in list_of_companies:
        raise HTTPException(status_code=404, 
        detail="404: Company not found. Mind case-sensitivity and use of spaces.")

    url = logos_dict[company_name]
    return get_dominant_color(url)


# -- legacy code -- 
# // # Returns the list of colors when the request body contains an url to the company logo.
# //@app.get("/{company_name}/colors", tags=["Logos"])
# // async def return_logo_colors(company_name: str) -> list:    
# //    for i in range(len(db)):
# //        if company_name == db[i]['name']:
# //            url_second_half = db[i]['logo']
# //            url = str(url_first_half + url_second_half)
# //            return get_dominant_color(url)
# //        else: 
# //            # ! Not safe. 
# //            # TODO: Add error handler.
# //            continue