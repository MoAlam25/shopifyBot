import requests 
import json

def write_to_file(json_obj):
    with open("shoe_info.json", "w") as f:
        json.dump(json_obj, f)


r = requests.get("https://shop-us.doverstreetmarket.com/products.json")
products = json.loads((r.text))['products']
shoes = []
final_shoes = {}

for product in products:
    if product['product_type'] == "Sneakers":
        final_shoes['vendor'] = product['vendor']
        final_shoes['shoe_sizes'] = {variant["title"]: variant["sku"] for variant in product["variants"]}


write_to_file(final_shoes)