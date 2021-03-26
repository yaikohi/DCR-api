from pydantic import BaseModel
from pydantic.types import Json


class Colors(BaseModel):
    primary_color: str
    secondary_color: str
    tertiary_color: str


class CompanyLogo(BaseModel):
    company_name: str
    colors: Colors