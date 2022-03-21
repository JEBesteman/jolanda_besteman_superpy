# Imports
import argparse
from datetime import datetime
import textwrap
from buy_func import buy_product
from date_func import advance_time, set_date_now
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

    ### argparse gedeelte ####
    parser = argparse.ArgumentParser(
        prog="SuperPy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
        WELCOME TO SUPERPY supermarket inventory tool!!

        CHOOSE ONE OF THE SUBCOMMANDS BELOW:
        For more information about these subcommands, check <subcommand> -h

        <set_date_now>          change 'system-today' to real-time today: yyyy-mm-dd
        <advance_time>          set 'today' to a specific date in future or past 
        <buy>                   buy product
        <sell>                  sell product
        <short_inventory>       show short inventory; product name and current stock
        <long_inventory>        show long inventory with all information of product
        <expired>               show all expired products till 'today'
        <revenue>               report/print revenue
        <profit>                report/print profit
        """,
        ),
    )
    parser.set_defaults(func=None)

    subparsers = parser.add_subparsers(
        dest="subparser_name",
    )
    # parser for real-time today
    set_date_now_parser = subparsers.add_parser(
        "set_date_now",
        description="Change the 'system'-date or reset date to real-time 'today'",
    )
    set_date_now_parser.add_argument(
        "date_now",
        help="change date to real-time today",
        action="store_true",
    )
    set_date_now_parser.set_defaults(func=set_date_now)

    # parser for advance time
    advance_time_parser = subparsers.add_parser(
        "advance_time",
        description="Set 'today' to specific date in future or past",
    )
    advance_time_parser.add_argument(
        "advance_time",
        help="set 'today' to a date in future or past: advance_time [number of days]",
        nargs=1,
        type=int,
    )
    advance_time_parser.set_defaults(func=advance_time)

    # parser for buy_product
    buy_parser = subparsers.add_parser(
        "buy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
        Buying product:
        Amount: default 1
        Syntax: buy [product_name] [price] [expiration_date] --amount [number or items]
        """
        ),
    )
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
        help="set amount of bought product (default: 1)",
    )
    buy_parser.set_defaults(func=buy_product)

    ## argparser for sell
    sell_parser = subparsers.add_parser(
        "sell",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
        Selling product:
        Amount: default 1 and maxmimum of 3
        Syntax: buy [product_name] [price] --amount [number or items]
        """
        ),
    )
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
        description="This is a short inventory; product_name and current stock",
    )
    short_inventory_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    short_inventory_parser.set_defaults(func=short_inventory)

    # parser for long_inventory
    long_inventory_parser = subparsers.add_parser(
        "long_inventory",
        parents=[date_parent_parser],
        description="This is a long inventory with all the information of product",
    )
    long_inventory_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    long_inventory_parser.set_defaults(func=long_inventory)

    # parser for show_expired_products
    expired_parser = subparsers.add_parser(
        "expired", description="Shows the expired products till 'today'"
    )
    expired_parser.add_argument(
        "--txt", action="store_true", help="exports to txt.file"
    )
    expired_parser.set_defaults(func=show_expired_products)

    # parser for revenue
    revenue_parser = subparsers.add_parser(
        "revenue",
        parents=[date_parent_parser],
        description="Shows revenue for date or period",
    )
    revenue_parser.add_argument(
        "--period",
        type=valid_date,
        nargs=2,
        help="choose period, [date1] - [date2], including both dates. Please enter dates: yyyy-mm-dd",
    )
    revenue_parser.set_defaults(func=show_revenue)

    # parser for profit
    profit_parser = subparsers.add_parser(
        "profit",
        parents=[date_parent_parser],
        description="Shows profit for date or period",
    )
    profit_parser.add_argument(
        "--period",
        type=valid_date,
        nargs=2,
        help="choose period, [date1] - [date2], including both dates. Please enter dates: yyyy-mm-dd",
    )
    profit_parser.set_defaults(func=get_profit)

    args = parser.parse_args()
    # print(args)

    if args.func:
        args.func(args)


if __name__ == "__main__":
    main()
