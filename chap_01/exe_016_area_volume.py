"""
The Program receives from the USER the MEASURE of a RADIUS "r"
and calculates the AREA of the CIRCLE and the VOLUME of the
SPHERE, having both radius "r".
"""

# IMPORT module MATH
import math


# Start Definition of FUNCTIONS


def valutaFloatPositive(numero):
    countPoints = 0
    for char in numero:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and numero != ".":
        if isinstance(float(numero), float) and float(numero) > 0:
            return True
    else:
        return False


def areaCircle(radius):
    area = math.pi * (radius ** 2)
    return area


def volumeSphere(radius):
    area = 4 / 3 * math.pi * (radius ** 3)
    return area


# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
radius = input("Enter the RADIUS of the CIRCLE and the SPHERE (cm): ")

numberFloatPositive = valutaFloatPositive(radius)

while not(radius.isdigit() and radius != "0") and not(numberFloatPositive):
    print("Incorrect entry. Try again.")
    radius = input("Enter the RADIUS of the CIRCLE and the SPHERE (cm): ")
    numberFloatPositive = valutaFloatPositive(radius)

# Conversion STR -> FLOAT
radius = float(radius)

# Computing the AREAS (Circle and Sphere)
areaCircle = areaCircle(radius)             # Area CIRCLE
volumeSphere = volumeSphere(radius)         # Area SPHERE

# Displaying the RESULTS
print("Area CIRCLE = %.2f" % areaCircle + " square centimeters")
print("Area SPHERE = %.2f" % volumeSphere + " cubic centimeters")