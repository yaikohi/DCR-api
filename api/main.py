from fastapi import FastAPI
# from pydantic import BaseModel
# from pydantic.types import Json
import json
import requests 

from core.schemas.schema import Colors
from util.dcr import get_dominant_color


# TODO: Create a PATCH request for updating the colors.
# TODO: Expand the documentation and for the api.

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

# Loading the databases
# Logos
db = "../data/db_logos.json"
db = json.load(open(db))

# Full
api_url = "https://dashboard-pio.herokuapp.com/companies"
request = requests.get(api_url).json()
db_api = request['response']

# !: Probably not very useful.
# # Returns the complete database
# @app.get("/", tags=["Database"])
# async def get_database():
#     return db_api

# Returns all the logo's.
@app.get("/logos", tags=["Logos"])
def get_logos():
    return db

# Returns the logo dict of a specific company specified in the url.
@app.get("/logos/{company_name}", tags=["Logos"])
async def get_colors(company_name: str) -> dict:
    return db[company_name]['logo']['colors']


# @app.patch("/logos/colors/{company_name}", tags=["Update Logo colours"])
# async def update_logo_colors(company_name: str, colors: Colors):
#     company_logo_url = db[company_name]['logo']['url']
#     # Uses kmeans clustering for retrieving the dominant colours in the image.
#     dominant_colors = get_dominant_color(company_logo_url)
#     colors['primary'] = dominant_colors[0]
#     colors['secondary'] = dominant_colors[1]
#     colors['tertiary'] = dominant_colors[2]

#     return colors