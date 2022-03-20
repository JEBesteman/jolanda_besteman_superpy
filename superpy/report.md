# Report SuperPy

## CSV

I have used the DictReader and DictWriter for readability and it is much easier to use. You can access keys/values with item["product_name"] instead of item[1]. Much easier to read!!

## Argparse

There are so many ways to use argparse. I have chosen for the use of *subparsers*, so that I can give subcommands to program. And *parent parser* for the dates (now, yesterday, date), because of the many times I reuse them. DRY code!

## Datetime

I have to check multiple times what the type was of the date. String, datetime.datetime object or datetime.date object. I have chosen to pass a datetime.date object to my functions that uses the dates arguments of subparsers. Because other wise you convert the dates over and over. This way it was more clear for my what to expect and where/when to convert.
And you need a datetime.date object for the best date comparison!

## Rich

You can do some much with Rich (and Coloroma) But I have decided for now, not to do too much with color. I'm going to do that later on!

## Other

I have chosen to use smaller functions that I can reused. Also it was easier to locate bugs. Also I use multiple files to break up the code for readability. I had once create a circulair import. That's why I create a date_file to fix that problem.
