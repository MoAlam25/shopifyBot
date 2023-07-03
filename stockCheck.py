import requests 
import json

def stockCheck():
    r = requests.get("https://shop-us.doverstreetmarket.com/products.json")
    products = json.loads((r.text))['products']


    for product in products:
        #print(product['title'])
        productname = product['title']

        if productname == 'Nike - Dunk Low SE NM2 - (FJ4610-702)':

            producturl = 'https://shop-us.doverstreetmarket.com/products/' + product['handle']
            return producturl
        
    return False