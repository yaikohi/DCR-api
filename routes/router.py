from fastapi import APIRouter

from routes import piodash, images


router = APIRouter()

router.include_router(piodash.router)
router.include_router(images.router)

@router.get("/", tags=["api"])
async def index():
    return 'You can view the endpoints of this api at /docs.'