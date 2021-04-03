"""
The program receives from the USER TWO POSITIVE INTEGER 
that REPRESENT the NUMERATOR and DENOMINATOR of a FRACTION
and returns (displaying it) the same FRACTION REDUCED to LOWEST TERMS.
"""


# START Definition of FUNCTIONS


def checkNumerator(numero):
    if numero.isdigit():
        return True
    return False


def checkDenominator(numero):
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


# Possible evolution -> IMPORT module
def computeGreatestCommonDivisor(number_1, number_2):
    gcd = number_1
    while (number_1 % gcd) != 0 or (number_2 % gcd) != 0:
        gcd -= 1
    return gcd


def reduceFractionLowestTerms(numerator, denominator):
    if (numerator == "0"):
        return "0"
    numerator = int(numerator)
    denominator = int(denominator)
    gcd = computeGreatestCommonDivisor(numerator, denominator)
    numerator_reduced = numerator // gcd
    denominator_reduced = denominator // gcd
    if denominator_reduced == 1:
        return numerator_reduced
    fraction_reduced = str(numerator_reduced) + "/" + \
        str(denominator_reduced)
    return fraction_reduced


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    numerator = input("Enter the NUMERATOR (positive) of a FRACTION: ")
    numerator_checked = checkNumerator(numerator)
    denominator = input("Enter the DENOMINATOR (positive > 0) of a FRACTION: ")
    denominator_checked = checkDenominator(denominator)

    while not(numerator_checked and denominator_checked):
        print("Incorrect entry. Try again.")
        numerator = input("Enter the NUMERATOR (positive) of a FRACTION: ")
        numerator_checked = checkNumerator(numerator)
        denominator = input(
            "Enter the DENOMINATOR (positive > 0) of a FRACTION: ")
        denominator_checked = checkDenominator(denominator)

    # FRACTIONS generation
    original_fraction = numerator + "/" + denominator
    fraction_reduced = reduceFractionLowestTerms(numerator, denominator)

    # Displaying the RESULTS
    print("The FRACTION ({}) reduced to LOWEST TERMS is equal to ({}).".format(
        original_fraction, fraction_reduced))


if __name__ == "__main__":
    main()
