"""
Create 2 functions: revenue for (specific) date, revenue for period (2 dates)
uses parameters now(today), yesterday, date of revenue_parser
or period and day1 and day2 of revenue_parser
"""

import csv
from date_func import string_to_dateobj, change_day


def get_revenue_date(day):
    with open("sold.csv", "r") as sold_file:
        csv_reader = csv.DictReader(sold_file)
        revenue = 0.00
        for line in csv_reader:
            sell_date = string_to_dateobj(line["sell_date"])
            if sell_date == day:
                revenue += float(line["sell_price"])
        return round(revenue, 2)


def get_revenue_between_dates(day1, day2):
    with open("sold.csv", "r") as sold_file:
        csv_reader = csv.DictReader(sold_file)
        revenue = 0.00
        for line in csv_reader:
            sell_date = string_to_dateobj(line["sell_date"])
            if sell_date >= day1 and sell_date <= day2:
                revenue += float(line["sell_price"])
        return round(revenue, 2)


# extra parameter (type_report), to determine when to print revenue or not
def show_revenue(args, type_report="revenue"):
    if args.now:
        day = change_day(0)
        revenue = get_revenue_date(day)
    if args.yesterday:
        day = change_day(-1)
        revenue = get_revenue_date(day)
    if args.date:
        day = args.date[0].date()
        revenue = get_revenue_date(day)
    if args.period:
        day1 = args.period[0].date()
        day2 = args.period[1].date()
        revenue = get_revenue_between_dates(day1, day2)
    if type_report == "revenue":
        if args.now:
            print(f"The revenue for today, {day}, is {revenue}")
        if args.yesterday:
            print(f"The revenue for yesterday, {day}, is {revenue}")
        if args.date:
            print(f"The revenue for {day} is {revenue}")
        if args.period:
            print(
                f"The revenue for periode from {day1} to including {day2} is {revenue}"
            )
    return revenue
