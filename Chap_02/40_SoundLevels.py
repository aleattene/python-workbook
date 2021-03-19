"""
The Program receives a CERTAIN NUMBER of DECIBELS from the USER
and returns (displaying it) the NAME of the possible associated NOISE.
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
        if 0 <= float(numero) <= 180:
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


def valutaIntValido(numero):
    if numero.isdigit():
        if 0 <= int(numero) <= 180:
            return True
    return False


def dbNoise(noise):
    if noise == 180:
        noise = "ROCKET TAKEOFF (180 dB)"
    elif 140 < noise < 180:
        noise = "between AIRPLANE TAKEOFF (140 dB) and the ROCKET TAKEOFF (180 dB)"
    elif noise == 140:
        noise = "AIRPLANE TAKEOFF (140 dB)"
    elif 130 < noise < 140:
        noise = "between the JACKHAMMER (130 dB) and the AIRPLANE TAKEOFF (140 db)"
    elif noise == 130:
        noise = "JACKHAMMER (130 dB)"
    elif 106 < noise < 130:
        noise = "between the GAS LAWNMOWER (106 dB) and the JACKHAMMER (130 dB)"
    elif noise == 106:
        noise = "GAS LAWNMOWER (106 dB)"
    elif 70 < noise < 106:
        noise = "between the ALARM CLOCK (70 dB) and the GAS LAWNMOWER (106 dB)"
    elif noise == 70:
        noise = "ALARM CLOCK (70 dB)"
    elif 40 < noise < 70:
        noise = "between the QUIET ROOM (40 dB) and the ALARM CLOCK (70 dB)"
    elif noise == 40:
        noise = "QUIET ROOM (40 dB)"
    elif 20 < noise < 40:
        noise = "between the RUSTLE of LIEAVES (20 dB) and the QUIET ROOM (40 dB)"
    elif noise == 20:
        noise = "RUSTLE of LIEAVES (20 dB)"
    elif 0 < noise < 20:
        noise = "between the TRESHOLD of HEARING (0 dB) and the RUSTLE of LIEAVES (20 dB)"
    elif noise == 0:
        noise = "TRESHOLD of HEARING (0 dB)"
    return noise


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
noise = input("Enter the NUMBER of DECIBELS (min 0 - max 180): ")
noiseIntValidated = valutaIntValido(noise)
noiseFloatValidated = valutaFloatValido(noise)

while not(noiseIntValidated or noiseFloatValidated):
    print("Incorrect entry. Try again.")
    noise = input("Enter the NUMBER of DECIBELS (min 0 - max 180): ")
    noiseIntValidated = valutaIntValido(noise)
    noiseFloatValidated = valutaFloatValido(noise)


# Conversion STR -> INT
noise = float(noise)


# Evaluation DECIBELS -> NOISE
typeNoise = dbNoise(noise)


# Displaying the RESULT
print("Similar NOISE = " + typeNoise)
