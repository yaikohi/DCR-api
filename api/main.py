from fastapi import FastAPI
import json
import requests 

from dcr import get_dominant_color


# Extra description for the api/docs.
tags_metadata = [
    {
        "name": "Logos",
        "description": "The logos of the companies in the database.",
    }
]


# Inside the api dir, use 'hypercorn main:app --reload'
app = FastAPI(
    title="DCR-api",
    description="For pioDash CMS.",
    version="0.1",
    openapi_tags=tags_metadata
)

# TODO: Stop using a local database. It was for testing only.
# Loading the company logo database from local storage
db = "../data/db_logos.json"
db = json.load(open(db))


# Returns company logos
@app.get("/", tags=["Logos"])
async def get_logos():
    return db


# Returns the logo dict of a specific company specified in the url.
@app.get("/{company_name}", tags=["Logos"])
async def get_logo_colors(company_name: str) -> dict:
    return db[company_name]['logo']['colors']


# Returns the list of colors when the request body contains an url to the company logo.
@app.get("/logos/{company_name}", tags=["Logos"])
async def return_logo_colors(company_name: str) -> list:
    
    data = requests.get("https://dashboard-pio.herokuapp.com/companies").json()['response']
    
    url_first_half = "https://dashboard-pio.herokuapp.com"
    
    for i in range(len(data)):
        if company_name == data[i]['name']:
            url_second_half = data[i]['logo']
            url = str(url_first_half + url_second_half)
            return get_dominant_color(url)
        else: 
            # ! Not safe. 
            # TODO: Add error handler.
            continue