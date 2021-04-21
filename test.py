# ? Learning story
# import requests

# url = "https://dashboard-pio.herokuapp.com/companies"
# response = requests.get(url).json()
# db = response['response']
# url_first_half = "https://dashboard-pio.herokuapp.com"

# # * Aswin's feedback:
# logos_dict = {company['name']: f"https://dashboard-pio.herokuapp.com{company['logo']}" for company in db}

# print(logos_dict)


# ! Trials below
# ? Pokemon API example; src: 
# async def main():
#     async with ClientSession() as session:
#         for number in range(1, 15):
#             pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
#             async with session.get(pokemon_url) as respOnse:
#                 pokemon = await respOnse.json()
#                 print(pokemon['name'])

# asyncio.run(main())


# ? Learning story
async def fetch_data():
    print(f'start fetch')
    await asyncio.sleep(0.01)

    print(f'done fetching')

async def print_nums():
    print(f'start print nums')
    for i in range(20):
        print(f'num: {i}')
        await asyncio.sleep(0.01)

async def main():
    start_time = time.time()


    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_nums())

    value1 = await task1
    print(value1)
    await task2
    print("It took %s seconds " % (time.time() - start_time))


asyncio.run(main())
