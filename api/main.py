from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json
import json

from core.schemas.schema import Colo                                                                                            rs

# Inside the api dir, use 'hypercorn main:app --reload'
app = FastAPI()                                                                                                                                                                                                                                                             

db = "../data/company_db.json"
db = json.load(open(db))


# Returns the complete database
@app.get("/")
async def index():
    return db


# Returns the attributes of a company specified in the URL
@app.get("/logos/{company_name}")
async def get_colors(company_name: "str"):
    for company in db:
        return db[company_name]


# TODO: Create a PATCH request for updating the colors.
# @app.post("/logos/{company_name}")
# async def update_logo_colors(color: Colors):
#     return color

# @app.patch("/logos/{company_name}")
# async def update_logo_colors(color: Colors):
#     db[company_name]['logo']['color'] = color


# ! Old, can probably be removed
# @app.get("/colors/{color_id}")
# async def read_color(color_id):
#     return {"color_id" : color_id}


# ! Doesn't work; can't find "Color" (it's in /core/schemas/schema.py)
# @app.post("/logos/{company_name}")
# async def add_color(color: Colors):
#     """Adds three colors to an id"""
#     db.append(color.dict())
#     return db[-1]