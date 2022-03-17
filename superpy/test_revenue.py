import csv

with open("sold.csv", "r") as sold_file:
    csv_reader = csv.DictReader(sold_file)
    revenue = 0
    for line in csv_reader:
        # print(line["sell_price"])
        revenue += float(line["sell_price"])
    print(round(revenue, 2))
