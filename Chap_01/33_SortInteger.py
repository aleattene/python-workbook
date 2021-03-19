"""
The Program receives from the USER 3 INTEGER
and displays them in ASCENDING ORDER.
"""

# START Definition of FUNCTION


def valutaInteger(numero):
    if numero.isdigit():
        return True
    return False


# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
print("Enter THREE INTEGERS.")
number1 = input("FIRST integer: ")
number2 = input("SECOND integer: ")
number3 = input("THIRD integer: ")

number1Validated = valutaInteger(number1)
number2Validated = valutaInteger(number2)
number3Validated = valutaInteger(number3)

while not(number1Validated and number2Validated and number3Validated):
    print("Incorrect entry. Try again.")
    print("Enter THREE INTEGERS.")
    number1 = input("FIRST integer: ")
    number2 = input("SECOND integer: ")
    number3 = input("THIRD integer: ")

    number1Validated = valutaInteger(number1)
    number2Validated = valutaInteger(number2)
    number3Validated = valutaInteger(number3)


# Conversion STR -> INT
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)


# Computing of the SUM of INTEGERS
numberMIN = min(number1, number2, number3)
numberMAX = max(number1, number2, number3)
numberMIDDLE = (number1 + number2 + number3) - numberMAX - numberMIN


# Displaying the RESULTS
print("SORTED INTEGERS -> " + str(numberMIN) + " - " +
      str(numberMIDDLE) + " - " + str(numberMAX))
