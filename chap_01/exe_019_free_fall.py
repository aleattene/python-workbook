""" 
The program receives from the USER the HEIGHT from which an OBJECT FALLS
and calculates its GROUND impact SPEED.
REFERENCE EQUATION:  Vf = sqrt(((Vi*2) + 2 * g * h)
- Vf = final speed
- Vi = initial speed (in this case Vi = 0)
- "g" = acceleration of gravity (9.81 m/s^2)
- "h" = height from which the object falls.
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


def speedFreeFall(Vinit, height):
    Vfinale = math.sqrt((Vinit**2) + 2 * 9.81 * height)
    return Vfinale


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
height = input("Enter the HEIGHT from which the object is DROPPED (meters): ")

heightFloatPositive = valutaFloatPositive(height)
heightIntPositive = valutaIntPositive(height)

while not(heightIntPositive or heightFloatPositive):
    print("Incorrect entry. Try again.")
    height = input(
        "Enter the HEIGHT from which the object is DROPPED (meters): ")
    heightFloatPositive = valutaFloatPositive(height)
    heightIntPositive = valutaIntPositive(height)

# Conversion STR -> FLOAT
height = float(height)

# GROUND SPEED computing
Viniziale = 0
Vfinale = speedFreeFall(Viniziale, height)          # GROUND impact SPEED 


# Displaying the RESULT
print("GROUND SPEED = %.2f" % Vfinale + " m/s = %.2f" %
      (Vfinale*3.6) + " Km/h")
