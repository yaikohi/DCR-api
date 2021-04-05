from fastapi import FastAPI
import requests 

# ? Pylance underlines this import with a warning but it compiles fine. ( "Import 'dcr' could not be resolved - PylancereportMissingImports" )
from dcr import get_dominant_color


# Description for the docs page. ( http://127.0.0.1:8000/docs )
tags_metadata = [
    {
        "name": "Logos",
        "description": "The logos of the companies in the database.",
    }
]


app = FastAPI(
    title="DCR-api",
    description="For pioDash CMS.",
    version="0.1",
    openapi_tags=tags_metadata
)


# ! LOADING THE NECESSARY DATA 
# Using a temporary memory-based database bypasses the need to create my own database.
# TODO: Double check the variable names for readability.
# TODO: Possible restrucuring of code.

data = requests.get("https://dashboard-pio.herokuapp.com/companies").json()['response']
url_first_half = "https://dashboard-pio.herokuapp.com"

list_of_logo_urls = []
list_of_companies = []
for i in range(len(data)):
    
    # list of companies
    company_name = data[i]['name']
    if company_name in list_of_companies:
        pass
    else:
        list_of_companies.append(company_name)
    
    # list of logo urls
    url = data[i]['logo']
    if url in list_of_logo_urls:
        pass
    else: 
        list_of_logo_urls.append(url_first_half+url)
    
logos_zip = zip(list_of_companies, list_of_logo_urls)
logos_dict = dict(logos_zip)
    



# ! API ROUTES BELOW
# Returns company logos
@app.get("/", tags=["Logos"])
async def get_logos():
    return data


# Returns the logo dict of a specific company specified in the url.
@app.get("/{company_name}", tags=["Logos"])
async def get_logo_colors(company_name: str) -> dict:
    for i in range(len(data)):
        if company_name == data[i]['name']:
            return data[i]


# TODO: Add a spelling check algorithm for the company names so that it corrects typos to the corresponding company name. This will make it more user-friendly.
# Returns the list of colors when the request body contains an url to the company logo.
@app.get("/{company_name}/colors", tags=["Logos"])
async def return_logo_colors(company_name: str) -> list:    
    if company_name in list_of_companies:
        url = logos_dict[company_name]
        
        return get_dominant_color(url)


# Old route, legacy code 
# // # Returns the list of colors when the request body contains an url to the company logo.
# //@app.get("/{company_name}/colors", tags=["Logos"])
# // async def return_logo_colors(company_name: str) -> list:    
# //    for i in range(len(data)):
# //        if company_name == data[i]['name']:
# //            url_second_half = data[i]['logo']
# //            url = str(url_first_half + url_second_half)
# //            return get_dominant_color(url)
# //        else: 
# //            # ! Not safe. 
# //            # TODO: Add error handler.
# //            continue