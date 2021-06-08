# The idea of this file is to create classes to replace the logic that exist in the current piodash endpoints for this API.
# Since I am still learning OOP it's very much still in development...

from typing import (Any, Callable, Coroutine, Dict, List,
                    Optional, Sequence, Type, Union)

from services.fetch_data import fetch_data


class PiodashEndpoint():
    def __init__(self, db):
        self.url: str = 'https://dashboard-pio.herokuapp.com/companies'
        self.db = fetch_data(self.url)['data']['response']
        self.url_base: str = 'https://dashboard-pio.herokuapp.com'

    @classmethod
    def get_url(self,
                logo_url_part: str,
                company_index: int = -0) -> str:

        company_index = company_index

        if company_index != -0:
            logo_url_part: str = self.db[company_index]['logo']
            return self.url_base + logo_url_part
        else:
            return self.url_base + logo_url_part


if __name__ == "__main__":
    print(PiodashEndpoint.get_url(
        logo_url_part='/companyLogos/Inergy.png', company_index=-0))
