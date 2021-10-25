"""
Write a program that computes the perimeter of a polygon.
Begin by reading the x and y coordinates
for the first point on the perimeter of the polygon from the user.
Then continue reading pairs of values
until the user enters a blank line for the x-coordinate.
Each time you read an additional coordinate
you should compute the distance to the previous point and add it to the perimeter.
When a blank line is entered for the x-coordinate
your program should add the distance from the last point back to the first point to the perimeter.
Then the perimeter should be displayed.
Sample input and output values are shown below.
The input values entered by the user are shown in bold.

Example:
Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the next x-coordinate (blank to quit): 1 Enter the next y-coordinate: 0
Enter the next x-coordinate (blank to quit): 0 Enter the next y-coordinate: 1
Enter the next x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373095
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
    if valutaFloat(numero) or valutaInteger(numero):
        return True
    return False


def computePointsDistance(x1, y1, x2, y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


# END Definition of FUNCTIONS


# Declaration of VARIABLES
perimeter = 0


# Acquisition and Control of the DATA entered by the USER
x1 = input("Enter the first x-coordinate: ")
y1 = input("Enter the first y-coordinate: ")
x1Validated = valutaEntry(x1)
y1Validated = valutaEntry(y1)

while not(x1Validated and y1Validated):
    print("Incorrect entry. Try again.")
    x1 = input("Enter the first x-coordinate: ")
    y1 = input("Enter the first y-coordinate: ")
    x1Validated = valutaEntry(x1)
    y1Validated = valutaEntry(y1)

x2 = input("Enter the second x-coordinate: ")
y2 = input("Enter the second y-coordinate: ")
x2Validated = valutaEntry(x2)
y2Validated = valutaEntry(y2)

while not(x2Validated and y2Validated):
    print("Incorrect entry. Try again.")
    x2 = input("Enter the second x-coordinate: ")
    y2 = input("Enter the second y-coordinate: ")
    x2Validated = valutaEntry(x2)
    y2Validated = valutaEntry(y2)

partialPerimeter = computePointsDistance(x1, y1, x2, y2)

x3 = input("Enter the third x-coordinate: ")
y3 = input("Enter the third y-coordinate: ")
x3Validated = valutaEntry(x3)
y3Validated = valutaEntry(y3)

while not(x3Validated and y3Validated):
    print("Incorrect entry. Try again.")
    x3 = input("Enter the third x-coordinate: ")
    y3 = input("Enter the third y-coordinate: ")
    x3Validated = valutaEntry(x3)
    y3Validated = valutaEntry(y3)

partialPerimeter += computePointsDistance(x2, y2, x3, y3)

x4 = input("Enter the next x-coordinate (empty line to quit): ")
if x4 != "":
    y4 = input("Enter the next y-coordinate: ")
    x4Validated = valutaEntry(x4)
    y4Validated = valutaEntry(y4)

while x4 != "":
    if (x4Validated and y4Validated):
        partialPerimeter += computePointsDistance(x3, y3, x4, y4)
        x3 = x4
        y3 = y4
        x4 = input("Enter the next x-coordinate (empty line to quit): ")
        if x4 != "":
            y4 = input("Enter the next y-coordinate: ")
            x4Validated = valutaEntry(x4)
            y4Validated = valutaEntry(y4)
    else:
        x4 = input("Enter the next x-coordinate (empty line to quit): ")
        if x4 != "":
            y4 = input("Enter the next y-coordinate: ")
            x4Validated = valutaEntry(x4)
            y4Validated = valutaEntry(y4)


# POLIGON PERIMETER computing
polygonPerimeter = partialPerimeter + computePointsDistance(x1, y1, x3, y3)


# Displaying the RESULT
print("The PERIMETER of the POLYGON is %.4f" % polygonPerimeter)
