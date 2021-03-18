"""
The Program receives from the USER a TEMPERATURE expressed in degrees CELSIUS
and returns the same TEMPERATURE expressed in both KELVIN and FAHRENHEIT degrees.
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


def celsiusFahrenheit(degreesCelsius):
    degreesFahrenheit = (degreesCelsius * 9 / 5) + 32
    return degreesFahrenheit


def celsiusKelvin(degreesCelsius):
    degreesKelvin = degreesCelsius + 273.15
    return degreesKelvin


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
degreesCelsius = input("Enter the TEMPERATURE (degrees Celsius): ")

degreesCelsiusValidated = validaEntry(degreesCelsius)

while not(degreesCelsiusValidated):
    print("Incorrect entry. Try again.")
    degreesCelsius = input("Enter the TEMPERATURE (degrees Celsius): ")
    degreesCelsiusValidated = validaEntry(degreesCelsius)


# Conversion STR -> FLOAT
degreesCelsius = float(degreesCelsius)


# Conversion Celsius -> Fahrenheit && Celsius -> Kelvin
degreesFahrenheit = celsiusFahrenheit(degreesCelsius)
degreesKelvin = celsiusKelvin(degreesCelsius)


# Displaying the RESULTS
print("RESULTS -> %.2f" % degreesCelsius + " °C = %.2f" % degreesFahrenheit +
      " °F alias %.2f" % degreesKelvin + " °K")


# Possible evolution -> check that the values are included in the respective scales
