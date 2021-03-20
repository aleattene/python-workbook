"""
The Program receives from the USER an ELECTROMAGNETIC FREQUENCY (GHz)
and returns the NAME of the corresponding RADIATION (Radio Wave, Microwave, etc).
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


def valutaFloatPositive(numero):
    if valutaFloat(numero):
        if float(numero) > 0:
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


def valutaIntPositive(numero):
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


def frequencyToRadiation(frequency):
    if frequency < 3 * (10 ** 9):
        radiation = "RADIO WAVES"
    elif 3 * (10 ** 9) <= frequency < 3 * (10 ** 12):
        radiation = "MICROWAVES"
    elif 3 * (10 ** 12) <= frequency < 4.3 * (10 ** 14):
        radiation = "INFRARED LIGHT"
    elif 4.3 * (10 ** 14) <= frequency < 7.5 * (10 ** 14):
        radiation = "VISIBLE LIGHT"
    elif 7.5 * (10 ** 14) <= frequency < 3 * (10 ** 17):
        radiation = "ULTRAVIOLET LIGHT"
    elif 3 * (10 ** 17) <= frequency < 3 * (10 ** 19):
        radiation = "X-RAYS"
    else:   # frequency >= 3 * ( 10 ** 19)
        radiation = "GAMMA RAYS"
    return radiation


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
frequency = input(
    "Enter the FREQUENCY (GHz) of the ELECTROMAGNETIC RADIATION: ")
frequencyIntValidated = valutaIntPositive(frequency)
frequencyFloatValidated = valutaFloatPositive(frequency)

while not(frequencyIntValidated or frequencyFloatValidated):
    print("Incorrect entry. Try again.")
    frequency = input(
        "Enter the FREQUENCY (GHz) of the ELECTROMAGNETIC RADIATION: ")
    frequencyIntValidated = valutaIntPositive(frequency)
    frequencyFloatValidated = valutaFloatPositive(frequency)


# Conversion STR -> FLOAT (Hz -> GHZ)
frequency = float(frequency) * (10 ** 9)


# Evaluation Frequency -> RADIATION
radiation = frequencyToRadiation(frequency)


# Displaying the RESULTS
print("The FREQUENCY " + str(frequency / (10 ** 9))  +
          " GHz is the ELECTROMAGNETIC frequency of the \"" + radiation + "\"")
