"""
The length of a month varies from 28 to 31 days.
In this exercise you will create a program that
reads the name of a month from the user as a string.
Then your program should display the number of days in that month.
Display “28 or 29 days” for February so that leap years are addressed.
Remember that:
- April, June, September, November = 30 days
- February = 28 or 29 days
- January, March, May, July, August, October, December = 31 days
"""

# START Definition of FUNCTIONS


def daysMonth(stringInput):
    month = stringInput.upper()
    if (month == "JANUARY") or (month == "MARCH") or (month == "MAY") or \
        (month == "JULY") or (month == "AUGUST") or (month == "OCTOBER") or \
            (month == "DECEMBER"):
        return "31"
    elif (month == "APRIL") or (month == "JUNE") or (month == "SEPTEMBER") or \
         (month == "NOVEMBER"):
        return "30"
    elif (month == "FEBRUARY"):
        return "28 or 29"
    else:
        return "error"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
stringInput = input("Enter the MONTH: ")
stringInputValidated = daysMonth(stringInput)

while (stringInputValidated == "error"):
    print("Incorrect entry. Try again.")
    stringInput = input("Enter the MONTH: ")
    stringInputValidated = daysMonth(stringInput)


# Computing of the DAYS that MAKE UP the MONTH
days = daysMonth(stringInput)


# Displaying the RESULTS
print(stringInput.upper() + " has " + days + " days")
