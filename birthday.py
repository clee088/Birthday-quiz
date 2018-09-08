"""
birthday.py
Author: Christopher Lee
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
todayyear = datetime.today().year


name = input("Hello, what is your name?")
month = input("Hi " + name + ", what was the name of the month you were born in?")
year = int(input("And what year were you born in, " + name + "?"))
day = input("And the day?")

if year >= 1980 and year <= 1989:
    gen = "eighties"
elif year >= 1990 and year <= 1999:
    gen = "nineties"
elif year >= 2000:
    gen = "two thousands"
elif year < 1980:
    gen = "Stone Age"

if month == "December" or month == "January" or month == "February":
    season = "winter"
else:
    if month == "March" or month == "April" or month == "May":
        season = "spring"
    else:
        if month == "June" or month == "July" or month == "August":
            season = "summer"
        else:
            if month == "September" or month == "October" or month == "November":
                season == "fall"

if month == "October" and day == 31:
    print("You were born on Halloween!")
elif month == todaymonth and day == todaydate:
    print("Happy birthday!")
else: print(name + ", you are a", season, "baby of the", gen, ".")

