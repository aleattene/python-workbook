"""
The Program receives from the user the environmental temperature 
(degrees Celsius) and wind speed (Km/h)
and calculates the WCI (Wind Chill Index).
"""

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


def valutaFloatValido(numero):
    if valutaFloat(numero):
        if float(numero) >= 4.8:
            return True
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


def valutaNumeroValido(numero):
    if valutaNumero(numero):
        if float(numero) <= 10:
            return True
    return False


def valutaIntPositive(numero):
    if numero.isdigit():
        if int(numero) >= 4.8:
            return True
    return False


def calcolaWCI(airTemp, windSpeed):
    WCI = 13.12 + (0.6215 * airTemp) - (11.37 * (windSpeed ** 0.16)) + \
        (0.3965 * airTemp * (windSpeed ** 0.16))
    return WCI


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the AIR TEMPERATURE and WIND SPEED.")
airTemp = input("AIR TEMPERATURE (max 10 degrees Celsius ): ")
windSpeed = input("WIND SPEED (min 4.8 kilometers per hour): ")

airTempNumeroValido = valutaNumeroValido(airTemp)
airTempFloatValido = valutaFloatValido(airTemp)
windSpeedIntPositive = valutaIntPositive(windSpeed)
windSpeedFloatValido = valutaFloatValido(windSpeed)

while not(airTempNumeroValido or airTempFloatValido) or \
        not(windSpeedIntPositive or windSpeedFloatValido):
    print("Incorrect entry. Try again.")
    print("Enter the AIR TEMPERATURE and WIND SPEED.")
    airTemp = input("AIR TEMPERATURE (max 10 degrees Celsius ): ")
    windSpeed = input("WIND SPEED (min 4.8 kilometers per hour): ")

    airTempNumeroValido = valutaNumeroValido(airTemp)
    airTempFloatValido = valutaFloatValido(airTemp)
    windSpeedIntPositive = valutaIntPositive(windSpeed)
    windSpeedFloatValido = valutaFloatValido(windSpeed)


# Conversion STR -> FLOAT
airTemp = float(airTemp)
windSpeed = float(windSpeed)


# WCI (WindChillIndex) Computing
WCI = calcolaWCI(airTemp, windSpeed)


# Displaying the RESULT
print("WIND CHILL Index (WCI) = %.1f" % WCI)
