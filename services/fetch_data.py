# # Asynchronous GETrequest to dashboard-pio.herokuapp
import aiohttp
import asyncio

async def fetch_data(url: str):
    """
    Asynchronously fetches data from the dashboard-pio.herokuapp 
    API. From the response it returns the data, the status code, 
    and the header as a dict.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            # print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            data = await response.json()
            return {"data": data['response'], "status": response.status, "headers": response.headers}

# if __name__ == "__main__":
#     data = asyncio.get_event_loop().run_until_complete(fetch_data(url="https://dashboard-pio.herokuapp.com/companies"))
#     print(data["data"][1]["id"])