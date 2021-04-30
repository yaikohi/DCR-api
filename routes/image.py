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

