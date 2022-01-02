# ------------------------------------------------------------
# -----------------**## SQLite Database ##**------------------

import sqlite3
import json
from pathlib import Path

# products = json.loads(Path("ecommerce/products.json").read_text())

# print(products)
# print(type(products))

# *-*-*-*-*-*-*-* Writing to a database
# with sqlite3.connect("products-db.sqlite3") as connection:
#     command = "INSERT INTO Products VALUES(?, ?, ?)"

#     for product in products:
#         connection.execute(command, tuple(product.values()))

#     connection.commit()

# https://sqlitebrowser.org/


# *-*-*-*-*-*-*-* Reading from a database
with sqlite3.connect("products-db.sqlite3") as connection:
    command = "SELECT * FROM Products"

    cursor = connection.execute(command)

    for data_row in cursor:
        print(data_row)
