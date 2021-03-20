"""
The Program receives from the USER a NUMERICAL EVALUATION related to an EMPLOYEE
and returns (displaying it) the corresponding assessment 
in a DESCRIPTIVE FORM (with the corresponding INCREASE in SALARY).
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


def floatValido(numero):
    if valutaFloatPositive(numero) or valutaIntValido:
        if (float(numero) == 0.0) or (float(numero) == 0.4) or float(numero) >= 0.6:
            return True
    return False


def valutaIntValido(numero):
    if numero.isdigit():
        if int(numero) >= 0:
            return True
    return False


def ratingToMeaning(rating):
    if rating == 0.0:
        return "UNACCEPTABLE"
    elif rating == 0.4:
        return "ACCEPTABLE"
    elif rating >= 0.6:
        return "MERITORIOUS"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
rating = input("Enter the RATING (0.0, 0.4, 0.6 or more): ")
ratingFloatValido = floatValido(rating)

while not(ratingFloatValido):
    print("Incorrect entry. Try again.")
    rating = input("Enter the RATING (0.0, 0.4, 0.6 or more): ")
    ratingFloatValido = floatValido(rating)


# Conversion STR -> FLOAT
rating = float(rating)


# Evalutation RATING -> MEANING && amount EMPLOYEE'S RAISE 
meaning = ratingToMeaning(rating)
amountRaise = rating * 2400.00


# Displaying the RESULTS
print("For RATING \"%.1f\"" % rating + " the PERFORMANCE of the EMPLOYEE is considered " +
      meaning + " (amount of the employee's RAISE $ %.2f" % amountRaise + ").")
