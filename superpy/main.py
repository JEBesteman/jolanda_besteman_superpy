# Imports
import argparse
from datetime import datetime
from buy_func import buy_product
from date_func import advance_time, date_now
from sell_func import sell_item
from inventory_func import short_inventory, long_inventory
from expired_func import show_expired_products
from revenue import show_revenue
from profit import get_profit


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # check if date is valid format yyyy-mm-dd
    def valid_date(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            msg = "Not a valid date: '{0}'.".format(date_str)
            raise argparse.ArgumentTypeError(msg)

    ## argparse gedeelte ####
    parser = argparse.ArgumentParser(
        description="Superpy supermarkt begint!", prog="SuperPy"
    )
    parser.set_defaults(func=None)

    subparsers = parser.add_subparsers(
        help="Kies 1 van onderstande mogelijkheden:", dest="subparser_name"
    )
    # parser for real-time today
    date_now_parser = subparsers.add_parser("date_now")
    date_now_parser.add_argument(
        "date_now",
        help="zet de systeem-date om in de realtime-date",
        action="store_true",
    )
    date_now_parser.set_defaults(func=date_now)

    # parser for advance time
    advance_time_parser = subparsers.add_parser("advance_time")
    advance_time_parser.add_argument(
        "advance_time",
        help="zet aantal dagen terug (-) of verder in tijd: advance_time [aantal dagen].",
        nargs=1,
        type=int,
    )
    advance_time_parser.set_defaults(func=advance_time)

    # parser for buy_product
    buy_parser = subparsers.add_parser("buy")
    buy_parser.add_argument("product_name", nargs=1, help="set product name")
    buy_parser.add_argument("price", type=float, nargs=1, help="set product buy price")
    buy_parser.add_argument(
        "expiration_date",
        type=valid_date,
        help="set expiration date of bought product in yyyy-mm-dd",
    )
    buy_parser.add_argument(
        "--amount",
        type=int,
        default=1,
        choices=range(1, 11),
        help="set amount of bought product (default: 1) with maximum of 10 items",
    )
    buy_parser.set_defaults(func=buy_product)

    ## argparser for sell
    sell_parser = subparsers.add_parser("sell")
    sell_parser.add_argument("product_name", nargs=1, help="set product name")
    sell_parser.add_argument(
        "sell_price", type=float, nargs=1, help="set product sell price"
    )
    sell_parser.add_argument(
        "--amount",
        type=int,
        default=1,
        choices=range(1, 4),
        help="set amount of sold product (default: 1) and maximum of 3",
    )
    sell_parser.set_defaults(func=sell_item)

    # extra parent_parser --> dates; now, yesterday, date
    date_parent_parser = subparsers.add_parser("date", add_help=False)
    date_parent_parser.add_argument(
        "--now", action="store_true", help="set date to 'today'"
    )
    date_parent_parser.add_argument(
        "--yesterday",
        action="store_true",
        help="set date to yesterday",
    )
    date_parent_parser.add_argument(
        "--date",
        type=valid_date,
        nargs=1,
        help="set date to specific date. Please enter date: yyyy-mm-dd",
    )

    # parser for short_inventory
    short_inventory_parser = subparsers.add_parser(
        "short_inventory",
        parents=[date_parent_parser],
        description="this is a short inventory, [product_name] [count]",
    )
    short_inventory_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    short_inventory_parser.set_defaults(func=short_inventory)

    # parser for long_inventory
    long_inventory_parser = subparsers.add_parser(
        "long_inventory",
        parents=[date_parent_parser],
        description="this is a long inventory with all the information of product",
    )
    long_inventory_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    long_inventory_parser.set_defaults(func=long_inventory)

    # parser for show_expired_products
    expired_parser = subparsers.add_parser(
        "expired", description="shows the expired products till 'today'"
    )
    expired_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    expired_parser.set_defaults(func=show_expired_products)

    # parser for revenue
    revenue_parser = subparsers.add_parser(
        "revenue",
        parents=[date_parent_parser],
        description="shows revenue for date or period",
    )
    revenue_parser.add_argument(
        "--period",
        type=valid_date,
        nargs=2,
        help="choose period, [day1] - [day2], including both dates. Please enter dates: yyyy-mm-dd",
    )
    revenue_parser.set_defaults(func=show_revenue)

    # parser for profit
    profit_parser = subparsers.add_parser(
        "profit",
        parents=[date_parent_parser],
        description="shows profit for date or period",
    )
    profit_parser.add_argument(
        "--period",
        type=valid_date,
        nargs=2,
        help="choose period, [day1] - [day2], including both dates. Please enter dates: yyyy-mm-dd",
    )
    profit_parser.set_defaults(func=get_profit)

    args = parser.parse_args()
    # print(args)

    if args.func:
        args.func(args)


if __name__ == "__main__":
    main()
