from fastapi import APIRouter, UploadFile, File

from services.dcr import get_dominant_colors, read_img

router = APIRouter()

@router.post("/colors/upload", tags=["colors"])
async def root(file: UploadFile = File(...)):
    return {"file": file}

@router.get("/colors/{img_url}", tags=["colors"])
async def get_colors(img_url: str) -> list:
    colors = get_dominant_colors(img_url)
    return colors
    
@router.get("/colors", tags=["colors"])
async def index():
    return 'Work in progress.'

