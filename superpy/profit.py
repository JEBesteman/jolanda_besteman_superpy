""" 
For profit you need the expenses (buy_price)
and the revenue
Profit = revenue - expenses
"""

# eerst expenses
import csv
from date_func import string_to_dateobj, change_day
from revenue import show_revenue


def get_expenses_date(datum):
    with open("bought.csv", "r") as bought_file:
        csv_reader = csv.DictReader(bought_file)
        expenses = 0.00
        for line in csv_reader:
            buy_date = string_to_dateobj(line["buy_date"])
            if buy_date == datum:
                expenses += float(line["buy_price"])
        return round(expenses, 2)


def get_expenses_between_dates(datum1, datum2):
    with open("bought.csv", "r") as bought_file:
        csv_reader = csv.DictReader(bought_file)
        expenses = 0.00
        for line in csv_reader:
            buy_date = string_to_dateobj(line["buy_date"])
            if buy_date >= datum1 and buy_date <= datum2:
                expenses += float(line["buy_price"])
        return round(expenses, 2)


def get_expenses(args):
    if args.now:
        datum = change_day(0)
        expenses = get_expenses_date(datum)
    if args.yesterday:
        datum = change_day(-1)
        expenses = get_expenses_date(datum)
    if args.date:
        datum = args.date[0].date()
        expenses = get_expenses_date(datum)
    if args.period:
        datum1 = args.period[0].date()
        datum2 = args.period[1].date()
        expenses = get_expenses_between_dates(datum1, datum2)
    return expenses


"""
alles omvattende functie profit """
# datum today, yesterday meengeven?


def get_profit(args):
    total_profit = show_revenue(args, type_report="profit") - get_expenses(args)
    profit = round(total_profit, 2)

    if args.now:
        datum = change_day(0)
        print(f"The profit for {datum} is {profit}")
    if args.yesterday:
        datum = change_day(-1)
        print(f"The profit for {datum} is {profit}")
    if args.date:
        print(f"The profit for {args.date[0].date()} is {profit}")
    if args.period:
        print(
            f"The profit for period between {args.period[0].date()} and {args.period[1].date()} is {profit}"
        )
