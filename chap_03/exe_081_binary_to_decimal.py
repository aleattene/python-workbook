"""
The program receives from the USER a BINARY NUMBER (base 2) 
and returns (displaying it) its EQUIVALENT DECIMAL NUMBER (base 10).
"""


# START Definition of the FUNCTION


def valutaEntry(binary):
    if binary.isdigit():
        for digit in binary:
            if digit != "0" and digit != "1":
                return False
        return True
    return False


def binaryToDecimal(binary):
    decimal = 0
    number_digits = len(binary)
    for position in range(number_digits):
        decimal += int(binary[position]) * (2**(number_digits-position-1))
    return decimal


# END Definition of the FUNCTION


# Acquisition and Control of the DATA entered by the USER
binary = input("Enter the BINARY NUMBER: ")
binary_validated = valutaEntry(binary)

while not(binary_validated):
    print("Incorrect entry. Try again.")
    binary = input("Enter the BINARY NUMBER: ")
    binary_validated = valutaEntry(binary)


# Computing BINARY NUMBER -> DECIMAL NUMBER
decimal = binaryToDecimal(binary)


# Displaying the RESULT
print("The BINARY NUMBER \"" + binary +
      "\" is equivalent to the DECIMAL NUMBER \"" + str(decimal) + "\"")
