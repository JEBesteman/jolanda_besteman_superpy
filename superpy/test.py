from date_func import get_date_today

# import datetime
from datetime import date

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


print(string_to_dateobj(today))


# string_obj = string_to_dateobj(today_string)
# exp_obj = string_to_dateobj(exp_string)
# if string_obj < exp_obj:
#     print("product is oke")
# else:
#     print("throw product away")
