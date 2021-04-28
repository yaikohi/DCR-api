# Testing

from fastapi import FastAPI

from core.config import (APP_NAME, APP_VERSION, API_KEY, API_PREFIX, IS_DEBUG)
from routes.router import router


def get_app() -> FastAPI:
    fast_api = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_api.include_router(router, prefix=API_PREFIX)
    
    return fast_api


app = get_app()