from date_func import get_date_today

# import datetime
from datetime import date, timedelta

# today_string = get_date_today()
# print(today_string)
# exp_string = "2022-03-09"
# date_object = datetime.date.fromisoformat(today_string)
# print(date_object)

today = get_date_today()


def string_to_dateobj(string):
    date_object = date.fromisoformat(string)
    print(type(date_object))
    return date_object


today_obj = string_to_dateobj(today)
print(today_obj)
delta1 = timedelta(days=1)
delta_yesterday = timedelta(days=-1)
print(today_obj + delta1)
print(today_obj + delta_yesterday)
print(type(today_obj + delta1))

# periode between date 2022-03-01 and today
# find date 2022-03-01
date_string = "2022-03-01"
date_new_object = string_to_dateobj(date_string)
print(date_new_object)
print(type(date_new_object))
print(date_new_object < today_obj)  # True
amount_days = today_obj - date_new_object
print(amount_days.days)  # 10 dagen tussen!!!


# string_obj = string_to_dateobj(today_string)
# exp_obj = string_to_dateobj(exp_string)
# if string_obj < exp_obj:
#     print("product is oke")
# else:
#     print("throw product away")

products_to_sell = [
    {
        "amount": "1",
        "buy_date": "2022-03-09",
        "expiration_date": "2022-03-12",
        "product_id": "1",
        "product_name": "bread",
        "product_price": "2.55",
        "sell_date": "2022-03-10",
        "sell_price": 3.45,
    },
    {
        "amount": "1",
        "buy_date": "2022-03-09",
        "expiration_date": "2022-04-09",
        "product_id": "2",
        "product_name": "bread",
        "product_price": "2.55",
        "sell_date": "2022-03-10",
        "sell_price": 3.45,
    },
]

# maar 1 product doorgeven
amount = 2
one_product = products_to_sell[:amount]
print(one_product)


# # remove buy_date and product_price key --> beide manier werken!
# for product in products_to_sell:
#     product.pop("buy_date")
#     del product["product_price"]
#     print(product)
