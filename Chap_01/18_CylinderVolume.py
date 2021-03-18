""" 
The Program receives from the USER, the RADIUS and HEIGHT
of a CYLINDER and calculates its VOLUME.
"""

# IMPORT module MATH
import math


# Start Definition of FUNCTIONS


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


def areaCircle(radius):
    area = math.pi * (radius ** 2)
    return area


def volumeCylinder(area, height):
    volume = area * height
    return volume


# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the RADIUS of the CYLINDER and its HEIGHT.")
radius = input("RADIUS (cm):")
height = input("HEIGHT (cm):")

radiusFloatPositive = valutaFloatPositive(radius)
heightFloatPositive = valutaFloatPositive(height)
radiusIntPositive = valutaIntPositive(radius)
heightIntPositive = valutaIntPositive(height)

while not(radiusIntPositive or radiusFloatPositive) or \
        not(heightIntPositive or heightFloatPositive):
    print("Incorrect entry. Try again.")
    print("Enter the RADIUS of the CYLINDER and its HEIGHT.")
    radius = input("RADIUS (cm):")
    height = input("HEIGHT (cm):")
    radiusFloatPositive = valutaFloatPositive(radius)
    heightFloatPositive = valutaFloatPositive(height)
    radiusIntPositive = valutaIntPositive(radius)
    heightIntPositive = valutaIntPositive(height)


# Conversion STR -> FLOAT
radius = float(radius)
height = float(height)


# Computing of CYLINDER VOLUME
areaBase = areaCircle(radius)                      # Area BASE CIRCLE
volume = volumeCylinder(areaBase, height)          # Cylinder Volume


# Displaying the RESULT
print("VOLUME CYLINDER = %.2f" % volume + " cubic centimeters")
