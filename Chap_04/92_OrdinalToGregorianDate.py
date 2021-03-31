"""
The program receives from the USER
the DATE (year, month and day) a PRODUCT was PURCHASED 
and returns (displaying it) the LAST HELPFUL DATE that it CAN BE RETURNED.
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


def ordinalDate(day, month, year):      # Possible evolution -> IMPORT
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


def gregorianDate(year, num_day):       # Possible evolution -> Refactoring
    if valutaLeapYear(str(year)):
        days_year = 366
        leap_year = 1
    else:
        days_year = 365
        leap_year = 0
    if num_day > days_year:
        year += 1
        num_day -= days_year
    if num_day <= 31:
        month = 1
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= (28 + leap_year):
        month = 2
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= (28 + leap_year)
    if num_day <= 31:
        month = 3
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= 30:
        month = 4
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 30
    if num_day <= 31:
        month = 5
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= 30:
        month = 6
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 30
    if num_day <= 31:
        month = 7
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= 31:
        month = 8
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= 30:
        month = 9
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 30
    if num_day <= 31:
        month = 10
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 31
    if num_day <= 30:
        month = 11
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    else:
        num_day -= 30
    if num_day <= 31:
        month = 12
        day = num_day
        return "{:04d}-{:02d}-{:02d}".format(year, month, day)
    return "OUT of RANGE"


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    print("Enter the DATE (year, month and day) a PRODUCT was PURCHASED.")
    year = input("YEAR: ")
    month = input("MONTH: ")
    day = input("DAY: ")
    yearValidated = valutaYear(year)
    monthValidated = validaMonth(month)
    dayValidated = valutaDay(day, month, year)

    while not(yearValidated and monthValidated and dayValidated):
        print("Incorrect entry. Try again.")
        print("Enter the DATE (year, month and day) a PRODUCT was PURCHASED.")
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
    date_purchased = ordinalDate(day, month, year)

    # Computing of the LAST HELPFUL DATE that a product can be returned
    return_deadline = date_purchased + 14
    return_date = gregorianDate(year, return_deadline)

    # Displaying the RESULTS
    print("Your PRODUCT can be RETURNED until " +
          return_date + " (14 days later purchase).")


if __name__ == "__main__":
    main()
