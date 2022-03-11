"""
All the functions needed for sell part
Uses the product_id to check if bought_item is already sold
(product_id is both class str!)
Sorted so that the earliest expiration date will be bought first
You can only sell product on date "today"
You get a discount of 30% when you sell product on its expiration date
"""
import csv
import pprint
from date_func import get_date_today


def get_bought_items():
    with open("bought.csv", "r") as bought_file:
        csv_reader = csv.DictReader(bought_file)
        bought_items = [row for row in csv_reader]
        return bought_items


def get_sold_ids():
    with open("sold.csv", "r") as sold_file:
        csv_reader = csv.DictReader(sold_file)
        sold_ids = [row["product_id"] for row in csv_reader]
        return sold_ids


# sell gebruikt alleen maar producten die "today" available zijn
def get_available_product(product_name):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date_today()
    for item in bought_items:
        # print(item["expiration_date"])
        if (
            item["product_id"] not in sold_ids
            and item["product_name"] == product_name
            and item["expiration_date"] >= today
        ):
            available_products.append(item)
    if len(available_products) == 0:
        print(f"Sorry, there are no available items found for {product_name}.")
    else:
        # sorteren op expiration date
        available_products_sorted = sorted(
            available_products, key=lambda x: x["expiration_date"]
        )
        return available_products_sorted


def sell_item(product_name, amount, sell_price):
    today = get_date_today()
    available_products = get_available_product(product_name)
    products_to_sell = []
    if available_products:
        if amount > len(available_products):
            print(
                f"Sorry, there are not enough items of {product_name} to buy, only {len(available_products)} item(s) left!"
            )
        else:
            for item in available_products:

                if item["expiration_date"] == today:
                    # pas de korting toe en voeg een 'sell price' key toe aan je dict.
                    item["sell_price"] = float(round(sell_price * 0.65, 2))
                    item["sell_date"] = today
                else:
                    # als niet today dan sell_price is die je geeft als argument in de functie
                    item["sell_price"] = sell_price
                    item["sell_date"] = today
                products_to_sell.append(item)  # voeg altijd item toe aan lijst

        # toevoegen aan sold.csv file
        pprint.pprint(products_to_sell)
        with open("sold.csv", "a", newline="") as sold_file:
            fieldnames = [
                "product_id",
                "product_name",
                "sell_price",
                "amount",
                "sell_date",
                "expiration_date",
                "product_price",
                "buy_date",
            ]

            csv_writer = csv.DictWriter(sold_file, fieldnames=fieldnames)
            csv_writer.writerows(products_to_sell)  # voeg de hele lijst toe aan je csv


sell_item(product_name="soup", amount=2, sell_price=1.95)
# sell_item("eggs", 1, 2.75)
