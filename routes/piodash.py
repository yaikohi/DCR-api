from fastapi import APIRouter
from concurrent.futures import ThreadPoolExecutor

from services.dcr import get_dominant_colors
from services.fetch_data import fetch_data

router = APIRouter()


# Necessary for fetching the logo-images from the other api.
url_base = "https://dashboard-pio.herokuapp.com"
url = "https://dashboard-pio.herokuapp.com/companies"

# Sync fetch
db = fetch_data(url)['data']['response']
id_set = []

@router.get("/piodash-colors/{company_id}", tags=["piodash-colors"])
async def get_colors_of_a_company(company_id: str) -> list:
    """
    Returns color values of a single company logo.
    """
    # TODO remove logic from this file.
    for company in db:
        if company_id == company['id']:
            url = url_base + company['logo']
            colors = get_dominant_colors(url)
            return colors
    return "Invalid 'company_id'."



@router.get("/piodash-colors/", tags=["piodash-colors"])
async def get_colors_of_companies() -> dict:
    """
    Returns color values of all the company logos in the piodash database.
    """
    piodash_colors = {}

    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(len(db)):
            company_name = db[i]['name']
            company_logo_url = url_base + db[i]['logo']

            try:
                company_colors = executor.submit(
                    get_dominant_colors, company_logo_url).result(timeout=29)
                piodash_colors[f'{company_name}'] = company_colors
            except Exception:
                piodash_colors[f'{company_name}'] = []
                print(Exception)
    return piodash_colors


@router.get("/piodash/ids/", tags=["piodash-colors"])
async def get_piodash_company_ids():
    """"
    Returns a dict with company names as keys 
    and id's as values.
    """
    piodash_id_dict = {}

    for i in range(len(db)):
        company_id = db[i]['id']
        company_name = db[i]['name']
        piodash_id_dict[f'{company_name}'] = company_id

    return piodash_id_dict
