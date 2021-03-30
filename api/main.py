from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json
import json

from core.schemas.schema import Colors

# @ the api dir, use 'hypercorn main:app --reload'
app = FastAPI()                                                                                                                                                                                                                                                             

db = "../data/db_full_logo_urls.json"
db = json.load(open(db))
# {"Fynch", {"blue", "red", "white"}}

@app.get("/")
async def index():
    return {"key": "value"}

@app.get("/colors")
async def get_colors():
    return db

@app.get("/colors/{color_id}")
async def read_color(color_id):
    return {"color_id" : color_id}

# ! Doesn't work; can't find "Color" (it's in /core/schemas/schema.py)
@app.post("/colors/{color_id}")
async def add_color(color: Colors):
    """Adds three colors to an id"""
    db.append(color.dict())
    return db[-1]