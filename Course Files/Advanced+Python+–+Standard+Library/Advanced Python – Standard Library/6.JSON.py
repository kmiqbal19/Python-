# ------------------------------------------------------------
# --------------------**## JSON Files ##**--------------------

import json
from pathlib import Path

products = [
    {"Product": "T-shirt", "Price": 5.99, "Stock Availability": 15},
    {"Product": "Jeans", "Price": 13.99, "Stock Availability": 8},
    {"Product": "Watch", "Price": 99.99, "Stock Availability": 4},
    {"Product": "Sweater", "Price": 29.99, "Stock Availability": 11},
]

products_data = json.dumps(products)
# print(products_data)


# writing the above data to a json file
# Path("ecommerce/products.json").write_text(products_data)


# reading from a json file

json_data = Path("ecommerce/products.json").read_text()

# print(json_data)

readable_data = json.loads(json_data)
# print(readable_data)
print(readable_data[0])
print(readable_data[0]["Product"])
print(readable_data[2]["Price"])
print(readable_data[3]["Stock Availability"])
