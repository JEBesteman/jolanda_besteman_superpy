from datetime import date, timedelta, datetime

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
def get_date_today():
    with open("date_file.txt", "r") as date_file:
        for line in date_file:
            # print("get date", line)
            return line


# to convert string to datetime object -> to compare dates better
def string_to_dateobj(date_str):
    date_object = date.fromisoformat(date_str)
    return date_object
