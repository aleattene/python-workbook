"""
The program receives TWO POSITIVE INTEGER numbers from the USER 
and returns (displaying it) their GREATEST COMMON DIVISOR
(using the EUCLID'S ALGORITHM).
"""


# START Definition of FUNCTIONS


def checkEntry(numero):     # possible evolution -> import module
    if numero.isdigit():
        if int(numero) >= 0:
            return True
    return False


def computeGreatestCommonDivisor(a, b):
    # EUCLID'S ALGORITHM
    if b == 0:
        return a
    else:
        c = a % b
        return computeGreatestCommonDivisor(b, c)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    entry = True
    while entry:
        number_1 = input("Enter the FIRST POSITIVE INTEGER NUMBER: ")
        number_2 = input("Enter the SECOND POSITIVE INTEGER NUMBER: ")
        if checkEntry(number_1) and checkEntry(number_2):
            entry = False

    # STRING TESTING
    # number_1 = "121439531096594251776"
    # number_2 = "3433683820292512484657849089281"

    # Conversion STR -> INT
    number_1 = int(number_1)
    number_2 = int(number_2)

    # Computing the Greater Common Divisor of number_1 and number_2
    gcd = computeGreatestCommonDivisor(number_1, number_2)

    # Displaying the RESULT
    print("The GREATEST COMMON DIVISOR of {} and {} is \"{}".format(
        number_1, number_2, gcd))


if __name__ == "__main__":
    main()
