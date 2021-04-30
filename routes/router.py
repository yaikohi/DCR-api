from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import asyncio
from routes import piodash

router = APIRouter()

router.include_router(piodash.router)
router.include_router(images.router)

# * Optional todos:
# TODO: 1. Learn jinja2. 
# TODO: 2. Add a new endpoint for a readme.md file.
# import markdown as md
# from fastapi.templating import Jinja2Templates


# templates = Jinja2Templates(directory="docs")
# # /API
# @router.get("/", tags=["readme"], response_class=HTMLResponse)
# async def show_readme(request: Request):
#     with open("./docs/README.md", "r", encoding="utf-8") as input_file:
#         text = input_file.read()
#     html = md.markdown(text)
#     data = {
#         "title": "Readme",
#         "text": html
#     }
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})
