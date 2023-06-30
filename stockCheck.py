import requests 
import json

r = requests.get(https://shop-us.doverstreetmarket.com/products.json)
products = json.loads((r.text))['products']

for product in products:
    print(products)