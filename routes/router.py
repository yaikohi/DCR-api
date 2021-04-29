from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

import asyncio
import markdown as md
from services.dcr import get_dominant_colors
from services.fetch_data import fetch_data

router = APIRouter()
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


# PIODASH IMAGES
# Necessary for fetching the logo-images from the other api.
url_base = "https://dashboard-pio.herokuapp.com"
response = asyncio.get_event_loop().run_until_complete(fetch_data(url="https://dashboard-pio.herokuapp.com/companies"))
db = response['data']

@router.get("/piodash-colors/{company_id}", tags=["piodash-colors"])
async def get_colors_of_a_company(company_id: str) -> list: 
    """
    Input: a company_id from the database.
    Output: returns a list of hexadecimal RGB color values
    """
    for i in range(len(db)):
        if company_id in db[i]['id']:
            url = url_base + db[i]['logo']
            colors = get_dominant_colors(url)
            return colors
        else:
            continue

@router.get("/piodash-colors/", tags=["piodash-colors"])
async def get_colors_of_a_company() -> dict: 
    """
    Returns a dict with key = company_name and,
    value = [logo_colors] where logo_colors is a list 
    containing three hexadecimal RGB color-values.
    Output: 
    """
    piodash_color_dict = {}
    
    for i in range(len(db)):
        company_name = db[i]['name']
        company_logo_url = url_base + db[i]['logo']
        try:
            company_colors = get_dominant_colors(company_logo_url)
        except:
            company_colors = f"Function 'get_dominant_colors' malfunctioned. Why tho"
        
        piodash_color_dict[f'{company_name}'] = company_colors
    return piodash_color_dict


@router.get("/piodash/", tags=["piodash-colors"])
async def get_piodash_db() -> dict:
    """
    Simply returns a database for now.

    Returns:
        dict: [the fetched-database]
    """
    return db


@router.get("/piodash/ids/", tags=["piodash-colors"])
async def get_piodash_company_ids():
    """"
    Returns a dict with company names as keys 
    and id's as values.
    
    Returns:
        dict: [key: company_name, value: company_id]
    """
    piodash_id_dict = {}
    
    for i in range(len(db)):
        company_id = db[i]['id']
        company_name = db[i]['name']
        piodash_id_dict[f'{company_name}'] = company_id

    return piodash_id_dict

asyncio.get_event_loop().close()
