import requests

url = "https://dashboard-pio.herokuapp.com/companies"
response = requests.get(url).json()

data = response['response']

print(type(data[0]['name']))    # str
print(type(data))               # list




for i in range(len(data)):
    company_name = 'Fynch'
    if data[i]['name'] == company_name:        
        logo_url_half = "https://dashboard-pio.herokuapp.com"
        logo_url_second_half = data[i]['logo']
        
        print(f'{logo_url_half + logo_url_second_half} it worked bro')
    
    
# logo_url_half = "https://dashboard-pio.herokuapp.com"
# logo_url_second_half = data[0]['logo']
# # logo_url = str(logo_url_half + logo_url_second_half)


# print(logo_url)