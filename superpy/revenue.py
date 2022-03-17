"""
create 2 functions: revenue of (specific) date, revenue over periode (2 dates)
uses parameters now(today), yesterday, date of revenue_parser
or periode and date1, date2 of revenue_parser
"""
# eerst alle inkomsten voor today
import csv
from date_func import string_to_dateobj, change_day


def get_revenue_date(datum):
    with open("sold.csv", "r") as sold_file:
        csv_reader = csv.DictReader(sold_file)
        revenue = 0.00
        for line in csv_reader:
            sell_date = string_to_dateobj(line["sell_date"])
            if sell_date == datum:
                revenue += float(line["sell_price"])
        return round(revenue, 2)


def get_revenue_between_dates(datum1, datum2):
    with open("sold.csv", "r") as sold_file:
        csv_reader = csv.DictReader(sold_file)
        revenue = 0.00
        for line in csv_reader:
            sell_date = string_to_dateobj(line["sell_date"])
            if sell_date >= datum1 and sell_date <= datum2:
                revenue += float(line["sell_price"])
        return round(revenue, 2)


""" alles omvattende functie
Note:
later aangeven of het voor revenue gebruikt, type_report == revenue
    - zo ja, dan printen hoeveel revenue op die dag of over periode is
"""


def show_revenue(args, type_report="revenue"):
    if args.now:
        datum = change_day(0)
        revenue = get_revenue_date(datum)
        print(revenue)
    if args.yesterday:
        datum = change_day(-1)
        revenue = get_revenue_date(datum)
        print(revenue)
    if args.date:
        datum = args.date[0].date()
        revenue = get_revenue_date(datum)
        print(revenue)
    if args.period:
        datum1 = args.period[0].date()
        datum2 = args.period[1].date()
        revenue = get_revenue_between_dates(datum1, datum2)
        print(revenue)
    if type_report == "revenue":
        if args.now:
            print(f"The revenue of {datum} is {revenue}")
        if args.yesterday:
            print(f"The revenue of {datum} is {revenue}")
        if args.date:
            print(f"The revenue of {datum} is {revenue}")
        if args.period:
            print(
                f"The revenue in periode from {datum1} to including {datum2} is {revenue}"
            )
