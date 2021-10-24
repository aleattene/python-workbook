"""
The Program receives from the USER a FREQUENCY of the FOURTH MUSICAL OCTAVE 
and returns the NAME of the associated MUSICAL note (margin of 1 Hz),
that is C4,D4,E4,F4,G4,A4,B4.
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
        if 260.63 <= float(numero) <= 494.88:
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
        if 261 <= int(numero) <= 494:
            return True
    return False


def frequencyToNote(frequency, margin):
    if (261.63 - margin) <= frequency <= (261.63 + margin):
        note = "C4"
    elif (293.66 - margin) <= frequency <= (293.66 + margin):
        note = "D4"
    elif (329.63 - margin) <= frequency <= (329.63 + margin):
        note = "E4"
    elif (349.23 - margin) <= frequency <= (349.23 + margin):
        note = "F4"
    elif (392.00 - margin) <= frequency <= (392.00 + margin):
        note = "G4"
    elif (440.00 - margin) <= frequency <= (440.00 + margin):
        note = "A4"
    elif (493.88 - margin) <= frequency <= (493.88 + margin):
        note = "B4"
    else:
        note = False
    return note


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
frequency = input(
    "Enter the FREQUENCY (Hz) of the NOTE (min 260.63 - max 494.88): ")
frequencyIntValidated = valutaIntValido(frequency)
frequencyFloatValidated = valutaFloatValido(frequency)


while not(frequencyIntValidated or frequencyFloatValidated):
    print("Incorrect entry. Try again.")
    frequency = input(
        "Enter the FREQUENCY (Hz) of the NOTE (min 260.63 - max 494.88): ")
    frequencyIntValidated = valutaIntValido(frequency)
    frequencyFloatValidated = valutaFloatValido(frequency)


# Conversion STR -> FLOAT
frequency = float(frequency)


# Evaluation Frequency -> NOTES
note = frequencyToNote(frequency, 1)


# Displaying the RESULT (float formatted with two decimal digits after comma)
if (note == False):
    print("Attention! There are NO NOTES with the entered FREQUENCY.")
else:
    print("The FREQUENCY %.2f" % frequency +
          " Hz is the frequency of the NOTE \"" + note + "\"")
