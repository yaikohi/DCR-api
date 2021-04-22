# Third party modules and libraries
from fastapi import FastAPI, HTTPException 
from dotenv import load_dotenv
import hypercorn
from hypercorn.config import Config

# Standard python modules
import os
import asyncio

# dcr-api modules
from services.dcr import *
from services.fetch_data import *


PORT = os.environ.get('port', 8000)
API_URL_DASHBOARDPIO = os.environ.get('API_URL_DASHBOARDPIO')

# Loads the .env file
# Prevents exposing sensitive data 
load_dotenv()

# Gets the url from the .env file
url = os.getenv('API_URL_DASHBOARDPIO')

# Description for the docs page (visible at http://127.0.0.1:8000/docs ).
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

if __name__ == "__main__":
    hypercorn.run(app, host="dcr-api000", port=port)


# Fetches the data from the database and constructs a local memory cache for queries.
# TODO: Add a HTTP error handler for the GETrequest.
loop = asyncio.get_event_loop()
api_response = loop.run_until_complete(fetch_data(url))

db = api_response["data"]

# Dict that stores all the logo-urls of every company: {"company_name": "logo_url"}. // # Thanks Aswin :)
company_logos_dict = {company['name']: f"https://dashboard-pio.herokuapp.com{company['logo']}" for company in db}

# Returns the full database.
@app.get("/", tags=["Companies"])
async def get_companies():
    return db


# TODO: Add a spelling check algorithm for the company names so that it corrects typos to the corresponding company name. This will make it more user-friendly.
# Returns the logo dict of a company specified in the url.
@app.get("/{company_name}", tags=["Companies"])
async def get_company_data(company_name: str) -> dict:

    # Raises an error when a typo occurs or the name is not in the database.    
    if company_name not in company_logos_dict.keys():
        raise HTTPException(status_code=404, 
        detail="404: Company not found. Mind case-sensitivity and use of spaces.")

    for i in range(len(db)):
        if company_name == db[i]['name']:
            return db[i]


# ? Add an endpoint to see the clusters in a graph?
# TODO: Add a spelling check algorithm for the company names so that it corrects typos to the corresponding company name. This will make it more user-friendly.
# Returns the list of colors when the request body contains an url to the company logo.
@app.get("/{company_name}/colors", tags=["Logos"])
async def get_logo_colors(company_name: str) -> list:

    # ? TODO: Create a error handler function in a seperate file.
    # Raises an error when a typo occurs or the name is not in the database.    
    if company_name not in company_logos_dict.keys():
        raise HTTPException(status_code=404, 
        detail="404: Company not found. Mind case-sensitivity and use of spaces.")

    company_logo_url = company_logos_dict[company_name]
    return get_dominant_color(company_logo_url)