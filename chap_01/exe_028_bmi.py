"""
The Program receives from the USER WEIGHT(kilograms) and HEIGHT(meters) of an INDIVIDUAL
and calculates the BMI (BodyMassIndex).
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


def bodyMassIndex(height, weight):
    BMI = weight / (height ** 2)
    return BMI


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the HEIGHT and WEIGHT.")
height = input("HEIGHT (meters): ")
weight = input("WEIGHT (kilograms): ")

heightIntPositive = valutaIntPositive(height)
heightFloatPositive = valutaFloatPositive(height)
weightIntPositive = valutaIntPositive(weight)
weightFloatPositive = valutaFloatPositive(weight)

while not(heightIntPositive or heightFloatPositive) or \
        not(weightIntPositive or weightFloatPositive):
    print("Incorrect entry. Try again.")
    print("Enter the HEIGHT and WEIGHT.")
    height = input("HEIGHT (meters): ")
    weight = input("WEIGHT (kilograms): ")

    heightIntPositive = valutaIntPositive(height)
    heightFloatPositive = valutaFloatPositive(height)
    weightIntPositive = valutaIntPositive(weight)
    weightFloatPositive = valutaFloatPositive(weight)


# Conversion STR -> FLOAT
height = float(height)
weight = float(weight)


# BMI (BodyMassIndex) Computing
BMI = bodyMassIndex(height, weight)


# Valuation BMI -> HEALTY
if BMI < 18.5:
    healty = "UNDERWEIGHT"
elif 18.5 <= BMI <= 25:
    healty = "HEALTY WEIGHT"
elif 25 < BMI < 30:
    healty = "OVERWEIGHT"
else:  # BMI >= 30
    healty = "OBESE"


# Displaying the RESULTS
print("BMI = %.2f" % BMI + " -> " + healty)
