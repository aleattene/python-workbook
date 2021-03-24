"""
The program receives from the USER a NUMBER (integer or float)
and returns (displaying it) its SQUARE ROOT,
computed with the NEWTON'S METHOD.
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


def valutaEntry(numero):
    if valutaFloatPositive(number) or valutaIntPositive(number):
        return True
    else:
        return False


# END Definition of FUNCTIONS


# Initialization of VARIABLE
goodApproximation = False


# Acquisition and Control of the DATA entered by the USER
number = input("Enter the NUMBER: ")
numberValidated = valutaEntry(number)

if numberValidated:
    number = float(number)      # Conversion STR -> FLOAT
    guess = number / 2          # Initialization of VARIABLE

while not(goodApproximation):
    if numberValidated:
        # Computing the PROGRESSIVE SQUARE ROOT
        guess = (guess + (number/guess)) / 2
        # Computing the PROGRESSIVE GOOD APPROXIMATION
        goodApproximation = abs((guess ** 2) - number) <= (10 ** (-12))
    else:
        print("Incorrect entry. Try again.")
        number = input("Enter the NUMBER: ")
        numberValidated = valutaEntry(number)
        if numberValidated:
            number = float(number)      # Conversion STR -> FLOAT
            guess = number / 2          # Initialization of VARIABLE


# Displaying the SQUARE ROOT computed
print("The SQUARE ROOT of %.2f" % number + " is approximately %.2f" % guess)


# Possible evolution:
# -> REFACTORING (checking input first and only then calculate the square root)
