"""
code needed for buy proces
use args parameter to get product information, which was given bought_subparser command
when product is bought, it is appended to bought.csv file
"""

import csv
from date_func import get_date_today


def get_product_id(file):
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        product_id = len(list(reader))
        return product_id


def buy_product(args):
    with open("bought.csv", "a", newline="") as bought_file:
        fieldnames = [
            "product_id",
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
                    "product_id": get_product_id("bought.csv") + i,
                    "product_name": args.product_name[0],
                    "buy_price": args.price[0],
                    "amount": 1,
                    "buy_date": get_date_today(),
                    "expiration_date": args.expiration_date.date(),
                }
            )
    print(f"product bought: {args.product_name}")
