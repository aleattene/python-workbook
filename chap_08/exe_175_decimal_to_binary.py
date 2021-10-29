"""
Write a recursive function that converts a non-negative decimal number to binary.

Treat 0 and 1 as base cases which return a string containing the appropriate digit.

For all other positive integers, n,
you should compute the next digit using the remainder operator and then
make a recursive call to compute the digits of n // 2.

Finally, you should concatenate the result of the recursive call (which will be a string) and
the next digit (which you will need to convert to a string) and return this string as the result of the function.

Write a main program that uses your recursive function
to convert a non-negative integer entered by the user from decimal to binary.
Your program should display an appropriate error message if the user enters a negative value.
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
