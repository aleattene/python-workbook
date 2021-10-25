"""
In this exercise you will create a program that
computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value
to indicate that no further values will be provided.
Your program should display an appropriate error message
if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the average.
"""

# START Definition of FUNCTIONS


def valutaFloat(numero):
    countPoints = 0
    for char in numero:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and numero != "." and valutaNumero(numero):
        if isinstance(float(numero), float):
            return True
    else:
        return False


def valutaNumero(numero):
    if numero == "":
        return False
    countSigns = 0
    for char in numero:
        if ord(char) == 45 or ord(char) == 43:
            countSigns += 1
    if ((numero[0] == "+") or (numero[0] == "-")) and countSigns == 1 and \
            numero != "-" and numero != "+" and numero != "-." and numero != "+.":
        return True
    elif numero[0].isdigit() and countSigns == 0:
        return True
    else:
        return False


def valutaInteger(numero):
    if len(numero) > 1:
        if numero.isdigit() or \
                (numero[0] == "-" and numero[1] != "0" and numero[1:].isdigit()):
            return True
    else:
        if numero.isdigit():
            return True
    return False


def valutaEntry(numero):
    if valutaFloat(number) or valutaInteger(number):
        return True
    else:
        return False

# END Definition of FUNCTIONS


# Declaration of VARIABLES
collectionValue = 0
items = 0


# Acquisition and Control of the DATA entered by the USER
number = input("Enter the VALUE: ")
while number == "0":
    print("WARNING, the ZERO VALUE CANNOT BE ENTERED as the FIRST value.")
    number = input("Enter the VALUE: ")

numberValidated = valutaEntry(number)

while number != "0":
    if numberValidated:
        collectionValue += float(number)
        items += 1
        number = input("Enter the VALUE: ")
        numberValidated = valutaEntry(number)
    else:
        print("Incorrect entry. Try again.")
        number = input("Enter the VALUE: ")
        numberValidated = valutaEntry(number)

# AVERAGE computing
average = collectionValue / items


# Displaying the RESULTS (Average of a Collection of values entered)
print("The AVERAGE of a Collection of VALUES entered is %.2f" % average)
