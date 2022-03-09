"""
code needed for buy proces
use args parameter to get product information, which was given bought_subparser command
when product is bought, it is appended to bought.csv file
"""

import csv
from main import get_date


def get_product_id():
    pass


def buy_product(args):
    with open("bought.csv", "a", newline="") as bought_file:
        fieldnames = [
            # "product_id",
            "product_name",
            "buy_price",
            "amount",
            "buy_date",
            "expiration_date",
        ]
        csv_writer = csv.DictWriter(bought_file, fieldnames=fieldnames)
        for i in range(args.amount):
            csv_writer.writerow(
                {
                    # product_id nog aanpassen
                    # "product_id":
                    "product_name": args.product_name[0],
                    "buy_price": args.price[0],
                    "amount": 1,
                    "buy_date": get_date(),
                    "expiration_date": args.expiration_date,
                }
            )
    print(f"product bought: {args.product_name}")
