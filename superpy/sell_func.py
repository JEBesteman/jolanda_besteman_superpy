"""
All the functions needed for sell part
Uses the product_id to check if bought_item is already sold
(product_id is both class str!)
Sorted so that the earliest expiration date will be bought first
You can only sell product on date "today"
You get a discount of 30% when you sell product on its expiration date
"""
import csv
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
        # print(sold_ids)
        return sold_ids


# sell gebruikt alleen maar producten die "today" available zijn
def get_available_product(product_name):
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    available_products = []
    today = get_date_today()
    for item in bought_items:
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


# print(get_available_product("bread"))
def sell_item(product_name, amount, sell_price):
    today = get_date_today()
    available_products = get_available_product(product_name)
    if available_products:
        if amount > len(available_products):
            print(
                f"Sorry, there are not enough items of {product_name} to buy, only {len(available_products)} item(s) left!"
            )
        else:
            for item in available_products:
                if item["expiration_date"] == today:
                    print("you get discount of 35% on original sell price")
                    sell_price *= 0.65
                    sell_price = float(round(sell_price, 2))
                    print(f"new sell_price is {sell_price}")
                else:
                    sell_price = sell_price
                    # toevoegen aan sold.csv file
        with open("sold.csv", "a", newline="") as sold_file:
            fieldnames = [
                "product_id",
                "product_name",
                "sell_price",
                "amount",
                "sell_date",
            ]
            csv_writer = csv.DictWriter(sold_file, fieldnames=fieldnames)
            for i in range(amount):
                csv_writer.writerow(
                    {
                        "product_id": available_products[i]["product_id"],
                        "product_name": product_name,
                        "sell_price": sell_price,
                        "amount": 1,
                        "sell_date": today,
                    }
                )
            print(f"product bought: {product_name} for {sell_price}.")


sell_item("soup", 1, 1.99)
