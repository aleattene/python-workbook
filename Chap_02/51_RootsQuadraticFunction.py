"""
The Program receives from the USER THREE CONSTANTS ("a", "b" and "c")
of a SECOND DEGREE EQUATION of the type:
a(x^2) + bx + c  (with "a" other than zero).
Afterwards, calculates any possible REAL SOLUTIONS.
"""

# IMPORT module MATH
import math


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


def valutaZero(numero):
    if numero.isdigit():
        if int(numero) == 0:
            return True
    elif len(numero) > 1:
        if valutaNumero(numero) and float(numero) == 0:
            return True
    return False


def correctEntry(numero):
    if valutaFloat(numero) or valutaNumero(numero):
        return True
    return False


def computesDiscriminant(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    return discriminant


def computesRoots(a, b, c):
    discriminant = computesDiscriminant(a, b, c)
    if discriminant < 0:
        return "NO REAL SOLUTION"
    elif discriminant == 0:
        x = (-b) / (2 * a)
        return "ONE REAL SOLUTION -> x = %.2f" % x
    else:
        x1 = ((-b) + math.sqrt(discriminant)) / (2 * a)
        x2 = ((-b) - math.sqrt(discriminant)) / (2 * a)
        return "TWO REAL SOLUTION -> x1 = %.2f" % x1 + " and x2 = %.2f" % x2


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the value for a (not equal), b and c: ")
a = input("a (non-zero): ")
b = input("b: ")
c = input("c: ")

aValidated = correctEntry(a)
bValidated = correctEntry(b)
cValidated = correctEntry(c)

while not(aValidated and bValidated and cValidated) or valutaZero(a):
    print("Incorrect entry. Try again.")
    print("Enter the value for a, b and c: ")
    a = input("a (non-zero): ")
    b = input("b: ")
    c = input("c: ")
    aValidated = correctEntry(a)
    bValidated = correctEntry(b)
    cValidated = correctEntry(c)


# Conversion STR -> FLOAT
a = float(a)
b = float(b)
c = float(c)


# DISCRIMINANT evaluation and ROOTS computing
roots = computesRoots(a, b, c)


# Displaying the RESULTS
print("RESULTS QUADRATIC FUNCTION: " + roots)
