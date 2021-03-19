"""
The Program receives from the USER a MONTH and a DAY of the year
and returns (displaying it) the corresponding season, knowing that:
- March 20 -> first day of Spring
- June 21 -> first day of Summer
- September 22 -> first day of Fall (or Autumn)
- December 21 -> first day of Winter
"""

# START Definition of FUNCTIONS


def validaMonth(stringInput):
    month = stringInput.upper()
    if (month == "JANUARY") or (month == "FEBRUARY") or (month == "MARCH") or \
        (month == "APRIL") or (month == "MAY") or (month == "JUNE") or \
        (month == "JULY") or (month == "AUGUST") or (month == "SEPTEMBER") or \
            (month == "OCTOBER") or (month == "NOVEMBER") or (month == "DECEMBER"):
        return True
    else:
        return False


def valutaIntValido(numero):
    if numero.isdigit():
        if 0 < int(numero) <= 31:    # Possible evolution: 28/30/31 days
            return True
    return False


def dateToSeason(month, day):
    month = month.upper()
    if (month == "DECEMBER" and day >= 21) or (month == "JANUARY") or \
            (month == "FEBRUARY") or (month == "MARCH" and day < 20):
        return "WINTER"
    elif (month == "MARCH" and day >= 20) or (month == "APRIL") or \
            (month == "MAY") or (month == "JUNE" and day < 21):
        return "SPRING"
    elif (month == "JUNE" and day >= 21) or (month == "JULY") or \
            (month == "AUGUST") or (month == "SEPTEMBER" and day < 22):
        return "SUMMER"
    else:
        return "FALL (or AUTUMN)"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the MONTH and DAY.")
month = input("MONTH: ")
day = input("DAY: ")
monthValidated = validaMonth(month)
dayIntValidated = valutaIntValido(day)

while not(monthValidated and dayIntValidated):
    print("Incorrect entry. Try again.")
    print("Enter the MONTH and DAY.")
    month = input("MONTH: ")
    day = input("DAY: ")
    monthValidated = validaMonth(month)
    dayIntValidated = valutaIntValido(day)


# Conversion STR -> INT
day = int(day)


# Evaluation DATE -> SEASON
season = dateToSeason(month, day)


# Displaying the RESULTS
print(month.upper() + " " + str(day) + " is a " + season + " day")
