"""
The Program receives from the USER a PRESSURE expressed in KILO-PASCALS (KP) and
returns the SAME PRESSURE expressed in POUNDS per SQUARE INCH (psi),
MILLIMETERS of MERCURY (mmHg) and ATMOSPHERES (atm).
"""

# START Definition of FUNCTIONS


def valutaFloat(numero):
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


def validaEntry(temperatura):
    if valutaNumero(temperatura) or valutaFloat(temperatura):
        return True
    return False


def KPtoPSI(pressureKP):
    pressurePSI = pressureKP * 0.1450377377
    return pressurePSI


def KPtoMMHG(pressureKP):
    pressureMMHG = pressureKP * 7.5006375542
    return pressureMMHG


def KPtoATM(pressureKP):
    pressureATM = pressureKP * 0.0099
    return pressureATM


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
pressureKP = input("Enter the PRESSURE (kilo-pascals): ")

pressureKPValidated = validaEntry(pressureKP)

while not(pressureKPValidated):
    print("Incorrect entry. Try again.")
    pressureKP = input("Enter the PRESSURE (kilo-pascals): ")
    pressureKPValidated = validaEntry(pressureKP)


# Conversion STR -> FLOAT
pressureKP = float(pressureKP)


# PRESSURE conversions
pressurePSI = KPtoPSI(pressureKP)    # kilo-pascals -> pounds per square inch
pressureMMHG = KPtoMMHG(pressureKP)  # kilo-pascals -> millimeters of mercury
pressureATM = KPtoATM(pressureKP)    # kilo-pascals -> atmospheres


# Displaying the RESULTS
print("RESULTS -> %.2f" % pressureKP + " kp = %.2f" % pressurePSI +
      " psi alias %.2f" % pressureMMHG + " mmHg alias %.2f" % pressureATM + " atm")
