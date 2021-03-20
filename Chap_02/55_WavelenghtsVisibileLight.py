"""
The Program receives from the USER a WAVELENGTH 
of the VISIBLE LIGHT SPECTRUM (380 -> 750 nm)
and returns (displaying it) the corresponding COLOR.
"""

# START Definition of FUNCTIONS


def valutaFloatPositive(numero):
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


def correctEntry(numero):
    if valutaFloatPositive(numero) or valutaIntValido:
        if 380 <= float(numero) <= 750:
            return True
    return False


def valutaIntValido(numero):
    if numero.isdigit():
        if 380 <= int(numero) <= 750:
            return True
    return False


def wavelengthToColor(wavelength):
    if 380 <= wavelength < 450:
        return "VIOLET"
    elif  450 <= wavelength < 495:
        return "BLUE"
    elif  495 <= wavelength < 570:
        return "GREEN"
    elif  570 <= wavelength < 590:
        return "YELLOW"
    elif  590 <= wavelength < 620:
        return "ORANGE"
    else:
        return "RED"    # Wavelength -> 620-750 nm


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
wavelength = input("Enter the WAVELENGTH (from 380 to 750 nm): ")
wavelengthValido = correctEntry(wavelength)

while not(wavelengthValido):
    print("Incorrect entry. Try again.")
    wavelength = input("Enter the WAVELENGTH (from 380 to 750 nm): ")
    wavelengthValido = correctEntry(wavelength)


# Conversion STR -> FLOAT
wavelength= float(wavelength)


# Identification WAVELENGTH -> COLOR
color = wavelengthToColor(wavelength)


# Displaying the RESULTS
print("Wavelength \"%.2f" % wavelength + " nm\" -> COLOR \"" + color + "\".")
