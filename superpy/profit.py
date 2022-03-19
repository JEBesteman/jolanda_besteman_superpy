""" 
For profit you need the expenses and the revenue
Profit = revenue - expenses
"""

import csv
from date_func import string_to_dateobj, change_day
from revenue import show_revenue


def get_expenses_date(day):
    with open("bought.csv", "r") as bought_file:
        csv_reader = csv.DictReader(bought_file)
        expenses = 0
        for line in csv_reader:
            buy_date = string_to_dateobj(line["buy_date"])
            if buy_date == day:
                expenses += float(line["buy_price"])
        return round(expenses, 2)


def get_expenses_between_dates(day1, day2):
    with open("bought.csv", "r") as bought_file:
        csv_reader = csv.DictReader(bought_file)
        expenses = 0
        for line in csv_reader:
            buy_date = string_to_dateobj(line["buy_date"])
            if buy_date >= day1 and buy_date <= day2:
                expenses += float(line["buy_price"])
        return round(expenses, 2)


def get_expenses(args):
    if args.now:
        day = change_day(0)
        expenses = get_expenses_date(day)
    if args.yesterday:
        day = change_day(-1)
        expenses = get_expenses_date(day)
    if args.date:
        day = args.date[0].date()
        expenses = get_expenses_date(day)
    if args.period:
        day1 = args.period[0].date()
        day2 = args.period[1].date()
        expenses = get_expenses_between_dates(day1, day2)
    return expenses


# type_report = "profit", so that you don't get extra print statements revenue
def get_profit(args):
    total_profit = show_revenue(args, type_report="profit") - get_expenses(args)
    profit = round(total_profit, 2)
    if args.now:
        day = change_day(0)
        print(f"The profit for today, {day}, is {profit}")
    if args.yesterday:
        day = change_day(-1)
        print(f"The profit for yesterday, {day}, is {profit}")
    if args.date:
        print(f"The profit for {args.date[0].date()} is {profit}")
    if args.period:
        print(
            f"The profit for period between {args.period[0].date()} and {args.period[1].date()} is {profit}"
        )
