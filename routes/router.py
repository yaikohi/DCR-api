from fastapi import APIRouter
import asyncio
from services.dcr import get_dominant_colors
from services.fetch_data import fetch_data

router = APIRouter()


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
    colors_list = []
    test = []
    # Loops over all the companies in the database
    for i in range(len(db)):
        # and checks for matches with the company_id
    #     while company_id != db[i]['id']:
    #         try:
    #             return f'Loading...'
    #         except company_id == db[i]['id']:
    #             colors_list.append(db[i]['id'])
    # return colors_list



@router.get("/piodash/", tags=["piodash-colors"])
async def get_piodash_db() -> dict:
    return db


@router.get("/piodash/ids/", tags=["piodash-colors"])
async def get_piodash_company_ids():
    id_list = []
    for i in range(len(db)):
        id_list.append(db[i]['id'])
    
    return id_list


asyncio.get_event_loop().close()
