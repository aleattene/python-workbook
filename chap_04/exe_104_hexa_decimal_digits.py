"""
Write two functions, hex2int and int2hex, that convert between
hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and
decimal (base 10) integers.
The hex2int function is responsible for converting a string containing a single hexadecimal digit to a base 10 integer,
while the int2hex function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit.
Each function will take the value to convert as its only parameter and return the converted value as its only result.
Ensure that the hex2int function works correctly for both uppercase and lowercase letters.
Your functions should display a meaningful error message and end the program
if the parameter’s value is outside of the expected range.
"""


# START Definition of the FUNCTIONS


def checkEntry(number):                 # Possible evolution -> IMPORT module
    if number.isdigit():
        type_number = "int_hex_number"  # Decimal or Hexadecimal number
    else:
        for i in range(len(number)):
            if (number[i].isdigit() or "A" <= number[i].upper() <= "F"):
                type_number = "hex_number"  # Hexadecimal number
            else:
                return "error"          # NOT Decimal or Hexadecimal number
    return type_number


def intToHex(int_number):               # NUMBER Conversion : DECIMAL -> HEXADECIMAL
    int_number = int(int_number)
    if int_number == 0:
        return "0"
    hex_number_tmp = []
    while int_number != 0:
        hex_digit = int_number % 16
        if 0 <= hex_digit <= 9:
            hex_number_tmp.append(str(hex_digit))
        else:        # 10 <= hex_digit <= 15:
            hex_number_tmp.append(chr(hex_digit + 55))
        int_number = int_number // 16
    hex_number = "".join(reversed(hex_number_tmp))
    return hex_number


def hexToInt(hex_number):               # NUMBER Conversion : HEXADECIMAL -> DECIMAL
    int_number = 0
    position = 0
    for i in reversed(hex_number):      # Possible evolution -> Refactoring (position)
        if "0" <= i <= "9":
            int_number += int(i) * (16 ** position)
        else:       # "A" <= hex_number[i] < "F":
            int_number += (int(ord(i.upper()))-55) * (16 ** position)
        position += 1
    return int_number


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the NUMBER (hexadecimal and/or decimal format): ")
    number_validated = checkEntry(number)

    while (number_validated == "error"):
        print("Incorrect entry. Try again.")
        number = input(
            "Enter the NUMBER (hexadecimal and/or decimal format): ")
        number_validated = checkEntry(number)

    # Displaying the CONVERSION RESULT
    print("The HEXADECIMAL NUMBER ({}) corresponds to the DECIMAL NUMBER ({}).".format(
        number, hexToInt(number)))
    if number_validated == "int_hex_number":
        print("The DECIMAL NUMBER ({}) corresponds to the HEXADECIMAL NUMBER ({}).".format(
            number, intToHex(number)))


if __name__ == "__main__":
    main()
