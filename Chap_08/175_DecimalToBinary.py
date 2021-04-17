"""
The program receives a NON-NEGATIVE INTEGER number from the USER 
and converts its to a BINARY number (using the RECURSION).
"""


# START Definition of FUNCTIONS


def checkEntry(number):     # possible evolution -> import module
    if number.isdigit():
        if int(number) >= 0:
            return True
    return False


def decimalToBinary(number):
    # BASE CASES (number = 0 or number = 1)
    if number < 2:
        return str(number)
    # RECURSIVE CASES (numbur >= 2)
    else:
        return decimalToBinary(number // 2) + str(number % 2)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    entry = True
    while entry:
        number = input("Enter the POSITIVE INTEGER NUMBER: ")
        if checkEntry(number):
            entry = False

    # CONVERSION Decimal number -> Binary number
    binary_digits = decimalToBinary(int(number))

    # Displaying the RESULT
    print("The DECIMAL NUMBER \"{}\" is equivalent to the BINARY NUMBER \"{}\"".format(
        number, binary_digits))


if __name__ == "__main__":
    main()
