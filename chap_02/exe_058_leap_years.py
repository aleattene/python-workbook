"""
The Program receives from the USER a YEAR
and returns (displaying it) if it's a LEAP YEAR or not.
"""

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if int(numero) != 0:
            return True
    return False


def valutaLeapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return "a LEAP YEAR"
    else:
        return "NOT a LEAP YEAR"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
year = input("Enter the YEAR you want know if it's a LEAP YEAR or not: ")
yearValidated = valutaIntPositive(year)

while not(yearValidated):
    print("Incorrect entry. Try again.")
    year = input("Enter the YEAR you want know if it's a LEAP YEAR or not: ")
    yearValidated = valutaIntPositive(year)


# Conversion STR -> INT
year = int(year)


# Evaluation if the year is a leap year or not
leapYear = valutaLeapYear(year)


# Displaying the RESULTS
print("The YEAR " + str(year) + " is " + leapYear + ".")
