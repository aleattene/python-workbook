"""
Write a function that determines how many days there are in a particular month.
Your function will take two parameters:
- the month as an integer between 1 and 12, and
- the year as a four digit integer.
Ensure that your function reports the correct number of days in February for leap years.
Include a main program that reads a month and year from the user and displays the number of days in that month.
"""

# START Definition of FUNCTIONS


def valutaYear(numero):                 # Possible evolution -> IMPORT
    if numero.isdigit() and len(numero) == 4:
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


def daysInMonth(month, year):
    month = int(month)
    if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or
            (month == 8) or (month == 10) or (month == 12)):
        return "31"
    elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
        return "30"
    elif (month == 2):
        if valutaLeapYear(year):
            return "29"
        elif not(valutaLeapYear(year)):
            return "28"


def monthDescription(month):
    months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
              "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return months[int(month)-1]


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    print("Enter a MONTH and a YEAR.")
    month = input("MONTH (1-12): ")
    year = input("YEAR (four digits): ")
    monthValidated = validaMonth(month)
    yearValidated = valutaYear(year)

    while not(monthValidated and yearValidated):
        print("Incorrect entry. Try again.")
        print("Enter a MONTH and a YEAR.")
        month = input("MONTH (1-12): ")
        year = input("YEAR (four digits): ")
        monthValidated = validaMonth(month)
        yearValidated = valutaYear(year)

    # Displaying the RESULTS
    print("In {} {} there are {} DAYS.".format(
        monthDescription(month), year, daysInMonth(month, year)))


if __name__ == "__main__":
    main()
