import csv
from rich.console import Console
from rich.table import Table
from sell_func import get_bought_items, get_sold_ids
from date_func import string_to_dateobj, get_date_today


today = get_date_today()


def get_expired_products():
    bought_items = get_bought_items()
    sold_ids = get_sold_ids()
    expired_products = []
    today_date = string_to_dateobj(today)
    for item in bought_items:
        exp_date_obj = string_to_dateobj(item["expiration_date"])
        buy_date_obj = string_to_dateobj(item["buy_date"])
        if (
            item["product_id"] not in sold_ids
            and buy_date_obj <= today_date
            and exp_date_obj < today_date
        ):
            expired_products.append(item)

    if len(expired_products) == 0:
        print(f"There are no producted wasted till {today_date}!")
    else:
        expired_products_sorted = sorted(
            expired_products, key=lambda x: x["expiration_date"]
        )
    return expired_products_sorted


def show_expired_products(args):
    expired_products = get_expired_products()
    with open(f"expired_{today}.csv", "w", newline="") as exp_file:
        fieldnames = [
            "product_id",
            "product_name",
            "buy_price",
            "amount",
            "buy_date",
            "expiration_date",
        ]
        csv_writer = csv.DictWriter(exp_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(expired_products)

    table = Table(title=f"Expired products till {today}", show_lines=True)

    table.add_column("Product ID", justify="right")
    table.add_column("Product name", style="magenta")
    table.add_column("Expiration date", justify="center", style="yellow")

    for item in expired_products:
        table.add_row(item["product_id"], item["product_name"], item["expiration_date"])

    console = Console(record=True)
    console.print(table)

    if args.txt:
        print("txt file created")
        console.save_text("expired.txt")
