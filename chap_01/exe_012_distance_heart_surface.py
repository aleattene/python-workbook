"""
The Program receives in INPUT from the USER the COORDINATES of TWO POINTS
on the Earth’s surface and computes their DISTANCE in Kilometers.
"""

# IMPORT module MATH (alias m)
import math as m


# Start Definition of FUNCTIONS


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


def distanceHeartSurface(t1, g1, t2, g2):
    distance = 6371.01 * \
        m.acos(m.sin(t1)*m.sin(t2) + m.cos(t1) * m.cos(t2) * m.cos(g1-g2))
    return distance

# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
t1 = input("Enter the LATITUDE of the FIRST POINT (degrees): ")
g1 = input("Enter the LONGITUDE of the FIRST POINT (degrees): ")
t2 = input("Enter the LATITUDE of the SECOND POINT (degrees): ")
g2 = input("Enter the LONGITUDE of the SECOND POINT (degrees): ")

numberFloatT1 = valutaFloat(t1)
numberFloatG1 = valutaFloat(g1)
numberFloatT2 = valutaFloat(t2)
numberFloatG2 = valutaFloat(g2)
numberTrueT1 = valutaNumero(t1)
numberTrueG1 = valutaNumero(g1)
numberTrueT2 = valutaNumero(t2)
numberTrueG2 = valutaNumero(g2)


while not(t1.isdigit() and g1.isdigit() and t2.isdigit() and g2.isdigit()) and \
    not(numberFloatT1 and numberFloatG1 and numberFloatT2 and numberFloatG2) and \
        not(numberTrueT1 and numberTrueG1 and numberTrueT2 and numberTrueG2):
    print("Incorrect entry. Try again.")
    t1 = input("Enter the LATITUDE of the FIRST POINT (degrees): ")
    g1 = input("Enter the LONGITUDE of the FIRST POINT (degrees): ")
    t2 = input("Enter the LATITUDE of the SECOND POINT (degrees): ")
    g2 = input("Enter the LONGITUDE of the SECOND POINT (degrees): ")

    numberFloatT1 = valutaFloat(t1)
    numberFloatG1 = valutaFloat(g1)
    numberFloatT2 = valutaFloat(t2)
    numberFloatG2 = valutaFloat(g2)
    numberTrueT1 = valutaNumero(t1)
    numberTrueG1 = valutaNumero(g1)
    numberTrueT2 = valutaNumero(t2)
    numberTrueG2 = valutaNumero(g2)


# Conversion DEGREES -> RADIANS
t1 = m.radians(float(t1))
g1 = m.radians(float(g1))
t2 = m.radians(float(t2))
g2 = m.radians(float(g2))

# Computing the DISTANCE
distanceHS = distanceHeartSurface(t1, g1, t2, g2)

# Displaying the RESULT
print("DISTANCE between the TWO POINTS = %.2f" % distanceHS + " kilometers")
