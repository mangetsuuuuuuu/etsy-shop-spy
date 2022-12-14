import json
import requests
import csv
from datetime import datetime
import pandas as pd
print('''
    ___________________  __
   / ____/_  __/ ___/\ \/ /
  / __/   / /  \__ \  \  / 
 / /___  / /  ___/ /  / /  
/_____/ /_/  /____/  /_/                              
                        By 0xSp3ar#5560
''')
store = input("Enter Store Name : ")
api_key = input("Enter Your Api : ")
uu = slice(0,-13)

print("Always Drink Water !! ")

try:
    r = requests.get(f'https://openapi.etsy.com/v2/shops/{store}?includes=Listings:active&api_key={api_key}').text
except:
    print("Somthing Wrong !! check Api or StoreName")
    exit()
data = json.loads(r)
Shop_Name=data['results'][0]['shop_name']
Shop_creation=str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(data['results'][0]['creation_tsz'])).date())
days=Shop_creation[uu]
ok =[f'Shop Name {Shop_Name}',f'Shop creation {days}']


try:
    r = requests.get(f'https://openapi.etsy.com/v2/shops/{store}/listings/active?&limit=100&api_key={api_key}').text
except:
    print("Somthing Wrong !! check Api or StoreName")
    exit()


data = json.loads(r)


slm = ['title','price','quantity','views','fav','creation','url','tags']

with open(f'{store}.csv' , 'a', encoding='utf8') as done:
        writer = csv.writer(done)
        writer.writerow(slm)
for i in data['results']:
    title=i.get('title')
    price=i.get('price')
    quantity=str(+i.get('quantity'))
    views=str(i.get('views'))
    fav = str(i.get('num_favorers'))
    date = str(pd.to_datetime(datetime.today()).date() - pd.to_datetime(datetime.fromtimestamp(i.get('original_creation_tsz'))).date())
    days=date[uu]
    url =i.get('url')
    tags =','.join(i['tags'])

    cool = [title,price,quantity,views,fav,days,url,tags]
    with open(f'{store}.csv' , 'a', encoding='utf8') as done:
        writer = csv.writer(done)
        writer.writerow(cool)
with open(f'{store}.csv' , 'a', encoding='utf8') as done:
        writer = csv.writer(done)
        writer.writerow(ok)
print("Done!!")
