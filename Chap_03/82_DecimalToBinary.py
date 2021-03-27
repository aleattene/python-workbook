"""
The program receives from the USER a DECIMAL NUMBER (base 10) 
and returns (displaying it) its EQUIVALENT BINARY NUMBER (base 2).
"""


# START Definition of the FUNCTION


def valutaEntry(number):
    if number.isdigit():
        if int(number) != 0:
            return True
    return False


def decimalToBinary(decimal):
    binary = []
    while decimal != 0:
        binary.append(str(decimal % 2))
        decimal = decimal // 2
    binary.reverse()    # reverse order of the list
    return binary


# END Definition of the FUNCTION


# Acquisition and Control of the DATA entered by the USER
decimal = input("Enter the DECIMAL NUMBER: ")
decimal_validated = valutaEntry(decimal)

while not(decimal_validated):
    print("Incorrect entry. Try again.")
    decimal = input("Enter the DECIMAL NUMBER: ")
    decimal_validated = valutaEntry(decimal)


# Computing DECIMAL NUMBER -> BINARY NUMBER
binary = decimalToBinary(int(decimal))


# Displaying the RESULT
print("The DECIMAL NUMBER \"" + decimal +
      "\" is equivalent to the BINARY NUMBER \"" + "".join(binary) + "\"")
