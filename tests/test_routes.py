from concurrent.futures.thread import ThreadPoolExecutor
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

piodash_colors = {}
piodash_logo_urls = []
piodash_names = []


def get_all_colors(dataB):
    """
    Creates a thread pool and extracts all the colors from the urls.
    """

    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(len(dataB)):
            company_name = dataB[i]['name']
            company_logo_url = url_base + dataB[i]['logo']

            try:
                company_colors = executor.submit(get_dominant_colors, company_logo_url).result(timeout=29)
                print(company_colors)
                piodash_colors[f'{company_name}'] = company_colors
            except Exception:
                piodash_colors[f'{company_name}'] = []
                print(Exception)
    return piodash_colors


@router.get("/test", tags=["piodash-colors"])
async def get_colors_of_companies() -> dict:
    """
    Returns color values of all the company logos in the piodash database.
    """
    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(len(db)):
            company_name = db[i]['name']
            company_logo_url = url_base + db[i]['logo']

            try:
                company_colors = executor.submit(get_dominant_colors, company_logo_url).result(timeout=29)
                piodash_colors[f'{company_name}'] = company_colors
            except Exception:
                piodash_colors[f'{company_name}'] = []
                print(Exception)
    return piodash_colors