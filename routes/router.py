from fastapi import APIRouter, Request

from routes import piodash, images


router = APIRouter()

router.include_router(piodash.router)
router.include_router(images.router)