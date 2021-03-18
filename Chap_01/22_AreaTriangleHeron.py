"""
The Program receives from the USER the length of the sides of a TRIANGLE
and calculates its AREA.
REFERENCE EQUATION (HERON'S FORMULA):  
AREA = sqrt(S * (S-s1) * (S-s2) * (S-s3))  
   S = (s1 + s2 + s3)
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


def areaTriangle(side1, side2, side3):
    side = (side1 + side2 + side3) / 2
    area = math.sqrt(side * (side - side1) * (side - side2) * (side - side3))
    return area


def verificaTriangle(side1, side2, side3):
    if side1 > (side2 + side3):
        return False
    if side2 > (side1 + side3):
        return False
    if side3 > (side2 + side1):
        return False
    return True


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the THREE SIDES of the TRIANGLE.")
side1 = input("FIRST SIDE (cm): ")
side2 = input("SECOND SIDE (cm): ")
side3 = input("THIRD SIDE (cm): ")
side1FloatPositive = valutaFloatPositive(side1)
side1IntPositive = valutaIntPositive(side1)
side2FloatPositive = valutaFloatPositive(side2)
side2IntPositive = valutaIntPositive(side2)
side3FloatPositive = valutaFloatPositive(side3)
side3IntPositive = valutaIntPositive(side3)

while not(side1IntPositive or side1FloatPositive) or \
    not(side2IntPositive or side2FloatPositive) or \
        not(side3IntPositive or side3FloatPositive):
    print("Incorrect entry. Try again.")
    print("Enter the THREE SIDES of the TRIANGLE.")
    side1 = input("FIRST SIDE (cm): ")
    side2 = input("SECOND SIDE (cm): ")
    side3 = input("THIRD SIDE (cm): ")

    side1FloatPositive = valutaFloatPositive(side1)
    side1IntPositive = valutaIntPositive(side1)
    side2FloatPositive = valutaFloatPositive(side2)
    side2IntPositive = valutaIntPositive(side2)
    side3FloatPositive = valutaFloatPositive(side3)
    side3IntPositive = valutaIntPositive(side3)

# Conversion STR -> FLOAT
side1 = float(side1)
side2 = float(side2)
side3 = float(side3)

# Verification of the EXISTENCE of the TRIANGLE
if (side1IntPositive or side1FloatPositive) and \
    (side2IntPositive or side2FloatPositive) and \
        (side3IntPositive or side3FloatPositive):
    triangoloVerified = verificaTriangle(side1, side2, side3)

while not(triangoloVerified):
    print("ATTENTION: the SUM of TWO SIDES cannot be greater than the THIRD." +
          "THIS TRIANGLE does NOT EXISTS. Try Again.")
    print("Enter the THREE SIDES of the TRIANGLE.")
    side1 = input("FIRST SIDE (cm): ")
    side2 = input("SECOND SIDE (cm): ")
    side3 = input("THIRD SIDE (cm): ")

    side1FloatPositive = valutaFloatPositive(side1)
    side1IntPositive = valutaIntPositive(side1)
    side2FloatPositive = valutaFloatPositive(side2)
    side2IntPositive = valutaIntPositive(side2)
    side3FloatPositive = valutaFloatPositive(side3)
    side3IntPositive = valutaIntPositive(side3)
    if (side1IntPositive or side1FloatPositive) and \
        (side2IntPositive or side2FloatPositive) and \
            (side3IntPositive or side3FloatPositive):
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)
        triangoloVerified = verificaTriangle(side1, side2, side3)

# Computing of the TRIANGLE AREA
area = areaTriangle(side1, side2, side3)

# Displaying the RESULT
print("AREA TRIANGLE = %.2f" % area + " square centimeters")
