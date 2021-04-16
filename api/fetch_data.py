# Asynchronous GETrequest to dashboard-pio.herokuapp
import aiohttp
import asyncio
import json
import time



async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        result = await response.json()
        return result

async def main():
    url = "https://dashboard-pio.herokuapp.com/companies"

    print(await fetch(url))

if __name__ == "__main__":
    # * Older versions of Python would use:
    # * asyncio.run(main())
    # * Src: https://stackoverflow.com/questions/65682221/runtimeerror-exception-ignored-in-function-proactorbasepipetransport
    asyncio.get_event_loop().run_until_complete(main())