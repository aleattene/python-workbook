"""
The Program receives from the USER a MONTH and a DAY of the year
and returns (displaying it) if this matches
to a CANADIAN NATIONAL HOLIDAY, knowing that:
- January 1 -> New Year’s Day
- July 1 -> Canada Day
- December 25 -> Christmas Day
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


def dateToHolyday(month, day):
    month = month.upper()
    if (month == "JANUARY") and (day == "1" or day == "01"):
        return "New Year's Day"
    elif (month == "JULY") and (day == "1" or day == "01"):
        return "Canada Day"
    elif (month == "DECEMBER"):
        return "Christams Day"
    else:
        return "error"


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


# Evaluation of CANADIAN NATIONAL HOLIDAY
holiday = dateToHolyday(month, day)


# Displaying the RESULTS
if holiday == "error":
    print("In Canada the date of " + month.upper() + " " +
          day + " does not match with a national holiday")
else:
    print("In Canada the date of " + month.upper() +
          " " + day + " matches with a " + holiday.upper())
