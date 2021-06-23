from concurrent.futures import ThreadPoolExecutor
import time

from services.dcr import get_dominant_colors
from services.fetch_data import fetch_data


def normal_example() -> dict:
    piodash_colors = {}
    url = "https://dashboard-pio.herokuapp.com/companies"
    db = fetch_data(url)['data']['response']
    url_base = "https://dashboard-pio.herokuapp.com"

    for i in range(len(db)):
        company_name = db[i]['name']
        company_logo_url = url_base + db[i]['logo']

        try:
            company_colors = get_dominant_colors(company_logo_url)
            piodash_colors[f'{company_name}'] = company_colors
        except Exception:
            piodash_colors[f'{company_name}'] = []
            print(Exception)
    
    return piodash_colors


def multithreading_example() -> dict:
    piodash_colors = {}
    url = "https://dashboard-pio.herokuapp.com/companies"
    db = fetch_data(url)['data']['response']
    url_base = "https://dashboard-pio.herokuapp.com"

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


if __name__ == '__main__':

    multithreading_start = time.perf_counter()
    multithreading_example()
    multithreading_finish = time.perf_counter()
    
    normal_start = time.perf_counter()
    normal_example()
    normal_finish = time.perf_counter()    

    print(f'Multithreaded function finished in {round(multithreading_finish-multithreading_start, 2)} seconds.\n\n Results: {multithreading_example()}\n\n\n')
    print(f'Normal function finished in {round(normal_finish-normal_start, 2)} seconds.\n\n Results: {normal_example()}\n\n\n')