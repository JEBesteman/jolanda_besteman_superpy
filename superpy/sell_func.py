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
from date_func import get_date_today, string_to_dateobj


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
    today_date_obj = string_to_dateobj(today)
    for item in bought_items:
        exp_date_obj = string_to_dateobj(item["expiration_date"])
        if (
            item["product_id"] not in sold_ids
            and item["product_name"] == product_name
            and exp_date_obj >= today_date_obj
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


def sell_item(args):
    today = get_date_today()
    today_date_obj = string_to_dateobj(today)
    available_products = get_available_product(args.product_name[0].lower())
    products_to_sell = []
    count = 0

    if available_products:
        if args.amount_item > len(available_products):
            print(
                f"Sorry, there are not enough items of {args.product_name} to buy, only {len(available_products)} item(s) left!"
            )
        else:
            for item in available_products:
                exp_date_obj = string_to_dateobj(item["expiration_date"])
                if count >= args.amount_item:
                    break
                if exp_date_obj == today_date_obj:
                    # pas de korting toe en voeg een 'sell price' key toe aan je dict.
                    item["sell_price"] = float(round(args.sell_price[0] * 0.65, 2))
                    item["sell_date"] = today
                else:
                    # als niet today dan sell_price is die je geeft als argument in de functie
                    item["sell_price"] = args.sell_price[0]  # args.sell_price
                    item["sell_date"] = today

                # voeg altijd item toe aan lijst
                products_to_sell.append(item)
                count += 1

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


# sell_item(product_name="soup", amount_item=2, sell_price=1.95)
# sell_item("Eggs", 1, 2.75)
# sell_item("Bread", 1, 3.10)
# sell_item(product_name="oatmeal", amount_item=3, sell_price=1.95)
# sell_item(product_name="Eggs", amount_item=1, sell_price=2.75)
