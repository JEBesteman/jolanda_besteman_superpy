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
from datetime import timedelta
from date_func import get_date_today, string_to_dateobj
from sell_func import get_bought_items, get_sold_ids
from pprint import pprint


# krijg je alle producten die op bepaalde datum gekocht zijn, maar niet verkocht en niet verlopen
def get_available_products(datum):  # datum_str
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    datum_date_obj = string_to_dateobj(datum)
    for item in bought_items:
        exp_date_obj = string_to_dateobj(item["expiration_date"])
        buy_date_obj = string_to_dateobj(item["buy_date"])
        if (
            item["product_id"] not in sold_ids
            and buy_date_obj <= datum_date_obj
            and exp_date_obj >= datum_date_obj
        ):
            available_products.append(item)

    if len(available_products) == 0:
        print(f"Sorry, there are no available items found for inventory")
    else:
        available_products_sorted = sorted(
            available_products, key=lambda x: x["product_name"]
        )
        pprint(available_products)
        return available_products_sorted


# short_inventory: van alle producten hoeveel aantal op voorrad
# -> product_name, count
## different datetime_objects, now(today), yesterday, (specific)date -> zie test.py


def short_inventory(args):
    if args.now is True:
        datum = get_date_today()
        # datum = string_to_dateobj(now)
    if args.date:
        # datum_obj = args.date[0].date()  # datetime.date object
        datum_obj = args.date[0]  # datetime.datetime object
        # print(type(datum_obj))
        datum = datum_obj.strftime("%Y-%m-%d")
        # print(type(datum))
    if args.yesterday:
        now = get_date_today()
        delta1 = timedelta(days=1)
        datum_obj = string_to_dateobj(now) - delta1
        # print(type(datum_obj))
        datum = datum_obj.strftime("%Y-%m-%d")
    products = get_available_products(datum)
    inventory = {}
    for product in products:
        if product["product_name"] in inventory.keys():
            inventory[product["product_name"]] += 1
        else:
            inventory.update({product["product_name"]: 1})
        pprint(inventory)

    with open((f"short_inventory_{datum}.csv"), "w", newline="") as short_file:
        fieldnames = ["product_name", "count"]
        csv_writer = csv.DictWriter(short_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for key, value in inventory.items():
            csv_writer.writerow({"product_name": key, "count": value})


# short_inventory(datum="2022-03-14")


# alle informatie van de producten in inventory
def long_inventory(datum):
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


# long_inventory(datum="2022-03-14")
