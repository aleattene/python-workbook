"""
Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2019-11-18
then your program should display a message indicating that
the day immediately after 2019-11-18 is 2019-11-19.
If the user enters values that represent 2019-11-30
then the program should indicate that the next day is 2019-12-01.
If the user enters values that represent 2019-12-31
then the program should indicate that the next day is 2020-01-01.
The date will be entered in numeric form with three separate input statements:
- one for the year,
- one for the month, and
- one for the day.
Ensure that your program works correctly for leap years.
"""

# START Definition of FUNCTIONS


def valutaYear(numero):
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


def valutaLeapYear(year):
    if year.isdigit():
        year = int(year)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False


def validaMonth(month):
    if month.isdigit():
        if 1 <= int(month) <= 12:
            return True
    return False


def valutaDay(day, month, year):
    if day.isdigit() and validaMonth:
        month = int(month)
        if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or
                (month == 8) or (month == 10) or (month == 12)) and (1 <= int(day) <= 31):
            return True
        elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)) and \
                (1 <= int(day) <= 30):
            return True
        elif (month == 2):
            if valutaLeapYear(year) and (1 <= int(day) <= 29):
                return True
            elif not(valutaLeapYear(year)) and (1 <= int(day) <= 28):
                return True
    return False


def nextDay(day, month, year):
    if 1 <= day <= 27:
        tomorrow = str(year) + "-%02d" % month + "-%02d" % (day + 1)
        return tomorrow
    elif day == 28:
        if month == 1 or 3 <= month <= 12:
            tomorrow = str(year) + "-%02d" % month + "-%02d" % (day + 1)
            return tomorrow
        elif month == 2:
            if valutaLeapYear(str(year)):
                tomorrow = str(year) + "-%02d" % month + "-%02d" % (day + 1)
                return tomorrow
            else:
                tomorrow = str(year) + "-%02d" % (month + 1) + "-01"
                return tomorrow
    elif day == 29:
        if month == 1 or 3 <= month <= 12:
            tomorrow = str(year) + "-%02d" % month + "-%02d" % (day + 1)
            return tomorrow
        elif month == 2:
            tomorrow = str(year) + "-%02d" % (month + 1) + "-01"
            return tomorrow
    elif day == 30:
        if (month == 1) or (month == 3) or (month == 5) or (month == 7) or \
                (month == 8) or (month == 10) or (month == 12):
            tomorrow = str(year) + "-%02d" % month + "-%02d" % (day + 1)
            return tomorrow
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
            tomorrow = str(year) + "-%02d" % (month + 1) + "-01"
            return tomorrow
    elif day == 31:
        if month != 12:
            tomorrow = str(year) + "-%02d" % (month + 1) + "-01"
            return tomorrow
        else:
            tomorrow = str(year + 1) + "-01-01"
            return tomorrow
    return "a day NOT FOUND"  # possible evolution: refactoring return


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the YEAR, MONTH and DAY.")
year = input("YEAR: ")
month = input("MONTH: ")
day = input("DAY: ")
yearValidated = valutaYear(year)
monthValidated = validaMonth(month)
dayValidated = valutaDay(day, month, year)

while not(yearValidated and monthValidated and dayValidated):
    print("Incorrect entry. Try again.")
    print("Enter the YEAR, MONTH and DAY.")
    year = input("YEAR: ")
    month = input("MONTH: ")
    day = input("DAY: ")
    yearValidated = valutaYear(year)
    monthValidated = validaMonth(month)
    dayValidated = valutaDay(day, month, year)


# Conversion STR -> INT
day = int(day)
month = int(month)
year = int(year)


# TOMORROW computing
tomorrow = nextDay(day, month, year)


# Displaying the RESULTS
print("Today is " + str(year) + "-%02d" % month + "-%02d" % day + ".")
print("Tomorrow will be " + tomorrow + ".")
