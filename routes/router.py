from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import asyncio
from routes import piodash

router = APIRouter()

router.include_router(piodash.router)

# TODO: 1. Seperate the endpoints. There are too many in this file now.

# * Optional todos:
# TODO: 2. Learn jinja2. 
# TODO: 3. Add a new endpoint for a readme.md file.
# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory="docs")
# # /API
# @router.get("/", tags=["readme"], response_class=HTMLResponse)
# async def show_readme(request: Request):
#     with open("./docs/README.md", "r", encoding="utf-8") as input_file:
#         text = input_file.read()
#     html = md.markdown(text)
#     data = {
#         "title": "Readme",
#         "text": html
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})

# IMAGES
@router.get("/colors/{img_url}", tags=["colors"])
async def get_colors(img_url: str) -> list:
    colors = get_dominant_colors(img_url)
    return colors
    
@router.get("/colors/", tags=["colors"])
async def get_colors(url: str) -> list:
    return get_dominant_colors(url)

