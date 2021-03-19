"""
The Program receives from the USER the MAGNITUDE of the RICHTER SCALE
and returns (displaying it) the corresponding EARTHQUAKE DESCRIPTION.
"""

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


def magnitudeToDescription(magnitude):
    if magnitude < 2.0:
        return "MICRO"
    elif 2.0 <= magnitude < 3.0:
        return "VERY MINOR"
    elif 3.0 <= magnitude < 4.0:
        return "MINOR"
    elif 4.0 <= magnitude < 5.0:
        return "LIGHT"
    elif 5.0 <= magnitude < 6.0:
        return "MODERATE"
    elif 6.0 <= magnitude < 7.0:
        return "STRONG"
    elif 7.0 <= magnitude < 8.0:
        return "MAJOR"
    elif 8.0 <= magnitude < 10.0:
        return "GREAT"
    else:
        return "METEORIC"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
magnitude = input("Enter the EARTHQUAKE MAGNITUDE: ")

magnitudeIntPositive = valutaIntPositive(magnitude)
magnitudeFloatPositive = valutaFloatPositive(magnitude)

while not(magnitudeIntPositive or magnitudeFloatPositive):
    print("Incorrect entry. Try again.")
    magnitude = input("Enter the EARTHQUAKE MAGNITUDE: ")

    magnitudeIntPositive = valutaIntPositive(magnitude)
    magnitudeFloatPositive = valutaFloatPositive(magnitude)


# Conversion STR -> FLOAT
magnitude = float(magnitude)


# Evaluation MAGNITUDE -> EARTHQUAKE Description
description = magnitudeToDescription(magnitude)


# Displaying the RESULTS
print("The EARTHQUAKE MAGNITUDE %.1f" % magnitude +
      " is considered a " + description + " earthquake")
