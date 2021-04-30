from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import asyncio

from routes import piodash

router = APIRouter()

router.include_router(piodash.router)
router.include_router(images.router)