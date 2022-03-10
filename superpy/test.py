from date_func import get_date_today

import datetime

today_string = get_date_today()
print(today_string)
exp_string = "2022-03-09"


def string_to_dateobj(string):
    date_object = datetime.date.fromisoformat(string)
    print(type(date_object))
    return date_object


string_obj = string_to_dateobj(today_string)
exp_obj = string_to_dateobj(exp_string)
if string_obj < exp_obj:
    print("product is oke")
else:
    print("throw product away")
