from pydantic import BaseModel
from pydantic.types import Json


class Colors(BaseModel):
    primary: str
    secondary: str
    tertiary: str


# class CompanyLogo(BaseModel):
#     company_name: str
#     colors: Colors