"""
Write a program that converts a decimal (base 10) number to binary (base 2).

Read the decimal number from the user as an integer and then
use the division algorithm shown below to perform the conversion.

When the algorithm completes, result contains the binary representation of the number.

Display the result, along with an appropriate message.

Let result be an empty string
Let q represent the number to convert
repeat
Set r equal to the remainder when q is divided by 2
Convert r to a string and add it to the beginning of result Divide q by 2,
discarding any remainder, and
store the result back into q until q is 0
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
