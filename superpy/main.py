# Imports
import argparse
import csv
from datetime import date, timedelta, datetime
from buy_func import buy_product

# from buy_func import buy_product

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    # date of "realtime-now"
    def date_now(args):
        today = date.today()
        date_today = datetime.strftime(today, "%Y-%m-%d")
        with open("date_file.txt", "w") as date_file:
            date_file.write(date_today)
            print(f"This is the real-time date of 'today': {date_today}")

    # advanced-time
    def advance_time(args):
        with open("date_file.txt", "r") as date_file:
            for line in date_file:
                old_date = datetime.strptime(line, "%Y-%m-%d")
                delta = timedelta(days=args.advance_time[0])
                new_date = datetime.strftime((old_date + delta), "%Y-%m-%d")
                print(f"this is the advance time of 'today', {new_date}")
            # now write new_date to date_file.txt file
            with open("date_file.txt", "w") as file:
                file.write(new_date)

    # get current date in date_file.txt
    def get_date():
        with open("date_file.txt", "r") as date_file:
            for line in date_file:
                print("get date", line)
                return line

    # check if date is valid format yyyy-mm-dd
    def valid_date(date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            msg = "Not a valid date: '{0}'.".format(date_str)
            raise argparse.ArgumentTypeError(msg)

    # def buy_product(args):
    #     with open("bought.csv", "a", newline="") as bought_file:
    #         fieldnames = [
    #             # "product_id",
    #             "product_name",
    #             "buy_price",
    #             "amount",
    #             "buy_date",
    #             "expiration_date",
    #         ]
    #         csv_writer = csv.DictWriter(bought_file, fieldnames=fieldnames)
    #         for i in range(args.amount):
    #             csv_writer.writerow(
    #                 {
    #                     # product_id nog aanpassen
    #                     # "product_id":
    #                     "product_name": args.product_name[0],
    #                     "buy_price": args.price[0],
    #                     "amount": 1,
    #                     "buy_date": get_date(),
    #                     "expiration_date": args.expiration_date,
    # of ....
    #                     "expiration_date": args.expiration_date.date(),

    #                 }
    #             )
    #     print(f"product bought: {args.product_name}")

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
        "--amount",
        type=int,
        default=1,
        help="set amount of bought product (default: 1)",
    )
    buy_parser.add_argument(
        "expiration_date",
        type=valid_date,
        help="set expiration date of bought product in yyyy-mm-dd",
    )
    buy_parser.set_defaults(func=buy_product)

    args = parser.parse_args()
    print(args)
    # date_now()
    # advanced_time(2)
    # get_date()
    if args.func:
        args.func(args)


if __name__ == "__main__":
    main()
