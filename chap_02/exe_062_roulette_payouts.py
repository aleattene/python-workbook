"""


"""

# IMPORT module RANDOM
import random


# START Definition of FUNCTIONS

def generatesNumber():
    number = random.randint(0, 37)
    return number


def overOrUnder(number):
    if 1 <= number <= 18:
        return "1 to 18"
    else:   # 19 <= number <= 36:
        return "19 to 36"


def redVsBlack(number):
    if 1 <= number <= 10 or 19 <= number <= 28:
        if number % 2 == 1:
            return "Red"
        else:
            return "Black"
    if 11 <= number <= 18 or 29 <= number <= 36:
        if number % 2 == 0:
            return "Red"
        else:
            return "Black"


def oddOrEven(number):
    if number % 2 == 1:
        return "Odd"
    else:
        return "Even"


# END Definition of FUNCTIONS


# NUMBER generation (RANDOM)
number = generatesNumber()

# NUMBER evaluation
if 1 <= number <= 36:
    redBlack = redVsBlack(number)
    oddEven = oddOrEven(number)
    overUnder = overOrUnder(number)

if number == 37:
    number = "00"

# Displaying the RESULTS
print("*******************")
print("     Number " + str(number) + "")
print("*******************")
print("***** PAYMENT *****")
if number == "00":
    print("- Pay 00")
elif number == 0:
    print("- Pay " + str(number))
else:
    print("- Pay " + str(number))
    print("- Pay " + redBlack)
    print("- Pay " + oddEven)
    print("- Pay " + overUnder)
print("*******************")
