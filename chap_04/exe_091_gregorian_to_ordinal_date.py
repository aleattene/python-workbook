"""
An ordinal date consists of a year and a day within it, both of which are integers.
The year can be any year in the Gregorian calendar while the day within the year ranges from one,
which represents January 1, through to 365 (or 366 if the year is a leap year) which represents December 31.
Ordinal dates are convenient when computing differences between dates that are a specific number of days
(rather than months).
For example, ordinal dates can be used to easily determine whether a customer is within a 90 day return period,
the sell by date for a food-product based on its production date, and the due date for a baby.

Write a function named ordinalDate that takes three integers as parameters.

These parameters will be a day, month and year respectively.
The function should return the day within the year for that date as its only result.
Create a main program that reads a day, month and year from the user and
displays the day within the year for that date.
Your main program should only run when your file has not been imported into another program.
"""

# START Definition of FUNCTIONS


def valutaYear(numero):                 # Possible evolution -> IMPORT
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


def valutaLeapYear(year):               # Possible evolution -> IMPORT
    if year.isdigit():
        year = int(year)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False


def validaMonth(month):                 # Possible evolution -> IMPORT
    if month.isdigit():
        if 1 <= int(month) <= 12:
            return True
    return False


def valutaDay(day, month, year):        # Possible evolution -> IMPORT
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


def ordinalDate(day, month, year):      # Possible evolution -> Refactoring
    ordinal_date = 0
    if valutaLeapYear(str(year)):
        leap_year = 1
    else:
        leap_year = 0
    if month == 1:
        ordinal_date += day
    else:
        ordinal_date += 31
    if month == 2:
        ordinal_date += day
    elif month > 2 and leap_year == 0:
        ordinal_date += 28
    elif month > 2 and leap_year == 1:
        ordinal_date += 29
    if month == 3:
        ordinal_date += day
    elif month > 3:
        ordinal_date += 31
    if month == 4:
        ordinal_date += day
    elif month > 4:
        ordinal_date += 30
    if month == 5:
        ordinal_date += day
    elif month > 5:
        ordinal_date += 31
    if month == 6:
        ordinal_date += day
    elif month > 6:
        ordinal_date += 30
    if month == 7:
        ordinal_date += day
    elif month > 7:
        ordinal_date += 31
    if month == 8:
        ordinal_date += day
    elif month > 8:
        ordinal_date += 31
    if month == 9:
        ordinal_date += day
    elif month > 9:
        ordinal_date += 30
    if month == 10:
        ordinal_date += day
    elif month > 10:
        ordinal_date += 31
    if month == 11:
        ordinal_date += day
    elif month > 11:
        ordinal_date += 30
    if month == 12:
        ordinal_date += day
    return ordinal_date


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    print("Enter the YEAR, MONTH and DAY of the GREGORIAN calendar.")
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

    # ORDINAL DATE computing
    today_ordinal = ordinalDate(day, month, year)

    # Displaying the RESULTS
    print("The date {:04d}-{:02d}-{:02d} in the Gregorian calendar corresponding".format(year, month, day),
          "at the DAY number {:02d} of the {:04d} (ORDINAL DATE).".format(today_ordinal, year))


if __name__ == "__main__":
    main()
