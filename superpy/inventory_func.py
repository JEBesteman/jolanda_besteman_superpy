"""
This are all functions needed to create the inventory of "today"/now, yesterday and on speicific date
I reuse some functions of sell_func.py, to get bougth_items, and sold_ids
I make 2 versions of inventiory:
    - short_inventory: product_name, count
        Show only how many items of product available are
    - long_inventory:
        Show all product information, sorted on product_name
"""
import csv
from rich.console import Console
from rich.table import Table
from date_func import string_to_dateobj, change_day
from sell_func import get_bought_items, get_sold_ids


# krijg je alle producten die op bepaalde datum gekocht zijn, maar niet verkocht en niet verlopen
# datetime.date object mee gegeven
def get_available_products(datum):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    for item in bought_items:
        exp_date_obj = string_to_dateobj(item["expiration_date"])
        buy_date_obj = string_to_dateobj(item["buy_date"])
        if (
            item["product_id"] not in sold_ids
            and buy_date_obj <= datum
            and exp_date_obj >= datum
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
    if args.now is True:
        datum = change_day(0)
    if args.date:
        datum = args.date[0].date()
    if args.yesterday:
        datum = change_day(-1)
    products = get_available_products(datum)
    inventory = {}
    for product in products:
        if product["product_name"] in inventory.keys():
            inventory[product["product_name"]] += 1
        else:
            inventory.update({product["product_name"]: 1})

    with open((f"short_inventory_{datum}.csv"), "w", newline="") as short_file:
        fieldnames = ["product_name", "count"]
        csv_writer = csv.DictWriter(short_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for key, value in inventory.items():
            csv_writer.writerow({"product_name": key, "count": value})

    table = Table(title="Short inventory for {datum}")

    table.add_column("Product name", style="magenta")
    table.add_column("Current stock", justify="right", style="green")

    for key, value in inventory.items():
        table.add_row(key, str(value))

    console = Console(record=True)
    console.print(table)

    if args.txt:
        console.save_text(f"short_inventory_{datum}.txt")


# all information of product in inventory
def long_inventory(args):
    if args.now is True:
        datum = change_day(0)
    if args.date:
        datum = args.date[0].date()
    if args.yesterday:
        datum = change_day(-1)
    products = get_available_products(datum)

    with open((f"long_inventory_{datum}.csv"), "w", newline="") as long_file:
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

    table = Table(title=f"long inventory for {datum}")

    table.add_column("Product ID", justify="right", style="green")
    table.add_column("Product name", style="magenta")
    table.add_column("buy price", justify="right", style="green")
    table.add_column("amount", justify="right", style="green")
    table.add_column("buy date", justify="right", style="green")
    table.add_column("expiration date", justify="right", style="green")

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
        console.save_text(f"long_inventory_{datum}.txt")
