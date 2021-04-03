"""
The program displays the MAGIC DATES in the 20th CENTURY (1901 - 2000)
considering that the MAGIC DATE is a date where
the DAY MULTIPLIED for the MONTH is equal to the TWO FINAL DIGITS YEAR. 
For example: June 10 , 1960 = 10 * 6 = 60 -> MAGIC DATE.
"""

# START Definition of FUNCTIONS


def valutaLeapYear(year):               # Possible evolution -> IMPORT
    if year.isdigit():
        year = int(year)
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False


def daysInMonth(month, year):           # Possible evolution -> IMPORT
    month = int(month)
    if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or
            (month == 8) or (month == 10) or (month == 12)):
        return 31
    elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
        return 30
    elif (month == 2):
        if valutaLeapYear(year):
            return 29
        elif not(valutaLeapYear(year)):
            return 28


def monthDescription(month):             # Possible evolution -> IMPORT
    months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
              "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return months[int(month)-1]


def magicDate():
    index = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            for day in range(1, daysInMonth(str(month), str(year))):
                if (day * month) == int(str(year)[2:]):
                    index += 1
                    month_description = monthDescription(month)
                    magic_date = "{:03d})  {} {:02d}, {:4d}".format(index,
                                                                    month_description, day, year)
                    print("|{:1s}".format("") +
                          "{:27s}|".format(magic_date))


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # MAGIC DATES display
    print("******************************")
    print("| MAGIC DATES - 20TH CENTURY |")
    print("******************************")
    magicDate()     # function call
    print("******************************")


if __name__ == "__main__":
    main()
