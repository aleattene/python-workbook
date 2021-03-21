"""
The Program receives from the USER a YEAR
and returns (displaying it) the DAY of the WEEK for JANUARY 1 of this YEAR,
considering the following formula:
dayOfTheWeek = (year + floor((year-1)/4)-flor((year-1)/100)+flor((year-1)/400))%7
"""

# IMPORT module MATH
import math as m

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if int(numero) != 0:
            return True
    return False


def nameDayWeek(year):
    daysWeek = {
        0: "SUNDAY",
        1: "MONDAY",
        2: "TUESDAY",
        3: "WEDNESDAY",
        4: "THURSDAY",
        5: "FRIDAY",
        6: "SATURDAY"
    }
    day = (year + m.floor((year - 1) / 4) - m.floor((year - 1) / 100)
           + m.floor((year - 1) / 400)) % 7
    nameDay = daysWeek.get(day)
    return nameDay


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
year = input(
    "Enter the YEAR for which you want to know the DAY of the WEEK for JANUARY 1: ")
yearValidated = valutaIntPositive(year)

while not(yearValidated):
    print("Incorrect entry. Try again.")
    year = input(
        "Enter the YEAR for which you want to know the DAY of the WEEK for JANUARY 1: ")
    yearValidated = valutaIntPositive(year)


# Conversion STR -> INT
year = int(year)


# Evaluation of the DAY of the WEEK for JANUARY 1 (year entered)
nameDayOfWeek = nameDayWeek(year)


# Displaying the RESULTS
print("The DAY of the WEEK for 1 JANUARY " +
      str(year) + " is \"" + nameDayOfWeek + "\".")
