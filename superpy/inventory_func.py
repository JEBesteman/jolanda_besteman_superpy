"""
Here are all functions needed to create the inventory of "today"/now, yesterday and on speicific date
I reuse some functions of sell_func.py, to get bougth_items, and sold_ids
I make 2 versions of inventiory:
    - short_inventory: product_name, count
        Show only how many items of product available are
    - long_inventory:
        Show all product information, sorted on product_name
Uses parameter "day" as a datetime.date object 
"""

import csv
from rich.console import Console
from rich.table import Table
from date_func import string_to_dateobj, change_day
from sell_func import get_bought_items, get_sold_ids


def get_available_products(day):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    for item in bought_items:
        exp_date_obj = string_to_dateobj(item["expiration_date"])
        buy_date_obj = string_to_dateobj(item["buy_date"])
        if (
            item["product_id"] not in sold_ids
            and buy_date_obj <= day
            and exp_date_obj >= day
        ):
            available_products.append(item)

    if len(available_products) == 0:
        print(f"Sorry, there are no available items found for inventory")
    else:
        available_products_sorted = sorted(
            available_products, key=lambda x: x["product_name"]
        )
        return available_products_sorted


# short_inventory: which product are in stock and how many
def short_inventory(args):
    if args.now:
        day = change_day(0)
    if args.date:
        day = args.date[0].date()
    if args.yesterday:
        day = change_day(-1)
    products = get_available_products(day)
    inventory = {}
    for product in products:
        if product["product_name"] in inventory.keys():
            inventory[product["product_name"]] += 1
        else:
            inventory.update({product["product_name"]: 1})

    with open((f"short_inventory_{day}.csv"), "w", newline="") as short_file:
        fieldnames = ["product_name", "count"]
        csv_writer = csv.DictWriter(short_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for key, value in inventory.items():
            csv_writer.writerow({"product_name": key, "count": value})

    table = Table(title=f"Short inventory for {day}", show_lines=True)

    table.add_column("Product name", style="magenta")
    table.add_column("Current stock", justify="center")

    for key, value in inventory.items():
        table.add_row(key, str(value))

    console = Console(record=True)
    console.print(table)

    if args.txt:
        console.save_text(f"short_inventory_{day}.txt")


# all information of product in inventory
def long_inventory(args):
    if args.now:
        day = change_day(0)
    if args.date:
        day = args.date[0].date()
    if args.yesterday:
        day = change_day(-1)
    products = get_available_products(day)

    with open((f"long_inventory_{day}.csv"), "w", newline="") as long_file:
        fieldnames = [
            "product_id",
            "product_name",
            "buy_price",
            "amount",
            "buy_date",
            "expiration_date",
        ]
        csv_writer = csv.DictWriter(long_file, fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(products)

    table = Table(title=f"long inventory for {day}", show_lines=True)

    table.add_column("Product ID", justify="right")
    table.add_column("Product name", style="magenta")
    table.add_column("Buy price", justify="right")
    table.add_column("Amount", justify="right", style="blue")
    table.add_column("Buy date", justify="center", style="green")
    table.add_column("Expiration date", justify="center", style="yellow")

    for item in products:
        table.add_row(
            item["product_id"],
            item["product_name"],
            item["buy_price"],
            item["amount"],
            item["buy_date"],
            item["expiration_date"],
        )

    console = Console(record=True)
    console.print(table)

    if args.txt:
        console.save_text(f"long_inventory_{day}.txt")
