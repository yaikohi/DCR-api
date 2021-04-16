import requests

url = "https://dashboard-pio.herokuapp.com/companies"
response = requests.get(url).json()
db = response['response']
url_first_half = "https://dashboard-pio.herokuapp.com"

# * Aswin's feedback:
logos_dict = {company['name']: f"https://dashboard-pio.herokuapp.com{company['logo']}" for company in db}

print(logos_dict)