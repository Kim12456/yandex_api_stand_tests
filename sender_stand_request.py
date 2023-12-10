import configuration
import requests
import data
def post_products_kits(ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json = ids)

response = post_products_kits(data.product_ids);
print(response.json())
print(response.status_code)