from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import Json

# @ the api dir, use 'hypercorn main:app --reload'
app = FastAPI()

db = open("../data/db_full_logo_urls.json")


@app.get("/")
async def index():
    return {"key": "value"}

@app.get("/colors")
async def get_colors():
    return db

@app.get("/colors/{color_id}")
async def read_color(color_id):
    return {"color_id" : color_id}

@app.post("/colors")
async def add_color(color: Color):
    db.append(color.dict())
    return db[-1]