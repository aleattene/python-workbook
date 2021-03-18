""" 
The Program receives from the USER the NUMBER of SIDES of a REGULAR POLYGON
(equal sides and angles included equal) and THEIR LENGTH and CALCULATES
the AREA of the POLYGON with the following formula::
AREA_POLIGONO = (number_sides * (length_side ^ 2) / (4 * tangent(pi / number_sides))
"""

# IMPORT module MATH
import math


# START Definition of FUNCTIONS


def valutaFloatPositive(numero):
    countPoints = 0
    for char in numero:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and numero != "." and valutaNumero(numero):
        if isinstance(float(numero), float) and float(numero) > 0:
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


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def areaPolygon(numSides, lengthSides):
    area = (numSides * (lengthSides ** 2)) / (4 * math.tan(math.pi / numSides))
    return area


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the NUMBER of SIDES of the POLYGON and their LENGHT.")
numSides = input("NUMBER of SIDES: ")
lengthSides = input("LENGHT of the SIDES (cm): ")

numSidesIntPositive = valutaIntPositive(numSides)
lengthSidesFloatPositive = valutaFloatPositive(lengthSides)
lengthSidesIntPositive = valutaIntPositive(lengthSides)

while not(numSidesIntPositive) or not(lengthSidesIntPositive or lengthSidesFloatPositive):
    print("Incorrect entry. Try again.")
    print("Enter the NUMBER of SIDES of the POLYGON and their LENGHT.")
    numSides = input("NUMBER of SIDES: ")
    lengthSides = input("LENGHT of the SIDES (cm): ")

    numSidesIntPositive = valutaIntPositive(numSides)
    lengthSidesFloatPositive = valutaFloatPositive(lengthSides)
    lengthSidesIntPositive = valutaIntPositive(lengthSides)


# Conversione STR -> FLOAT
numSides = float(numSides)
lengthSides = float(lengthSides)


# Computing of the POLYGON AREA
area = areaPolygon(numSides, lengthSides)


# Displaying the RESULT
print("AREA POLYGON = %.2f" % area + " square centimeters")
