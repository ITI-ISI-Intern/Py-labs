import json
import os

from decorator_task import log_time 

"""
Product Data Transformer (lambda, map, filter, zip)
   - Ask user for a list of product names (comma-separated).
   - Ask user for a list of product prices (comma-separated).
   - Process them by:
        - Pairing product with price.
        - Filtering out items where price <= 0.
        - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
   - Save the final result as JSON into "products.json".
   - Print a preview of the first 5 results.
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@log_time
def productDataTransformer():
    product_names = input("Enter product names (comma-separated): ").split(',')
    while True:
        try:
            product_prices = list(map(float, input("Enter product prices (comma-separated): ").split(',')))
            break
        except ValueError:
            print("Invalid input for prices. Please enter numeric values.")
            return
        
    
    paired_products = zip(product_names, product_prices)

    filtered_products = filter(lambda x: x[1] > 0, paired_products)

    transformed_products = map(lambda x: {"product": x[0], "price": x[1], "discounted": round(x[1] * 0.9, 2)}, filtered_products)

    
    final = list(transformed_products)
    json_data = json.dumps(final, indent=4)

    file_path = os.path.join(BASE_DIR, "files/products.json")
    with open(file_path, "w") as f:
        f.write(json_data)

# productDataTransformer()
