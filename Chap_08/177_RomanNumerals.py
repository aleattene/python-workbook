"""
The program receives a ROMAN number from the USER
and converts it to an INTEGER.
"""


# START Definition of FUNCTIONS


def checkEntry(roman_numeral):
    roman_numerals = ["M", "D", "C", "L", "X", "V", "I"]
    for letter in roman_numeral:
        if letter.upper() not in roman_numerals:
            return False
    return True


def romanToInteger(roman_number, previous_letter):
    # DICTIONARY - Roman Numerals
    roman_numerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    # BASE CASE (empty list)
    if roman_number == []:
        return 0
    # RECURSIVE CASES (each recursive case remove first char of the tail)
    tail = roman_number[1:len(roman_number)]
    # Decimal Value of the FIRST CHAR of the list
    value = roman_numerals[roman_number[0]]
    # Comparison of PRESENT value with PREVIOUS value
    if value >= previous_letter:
        # present value GREATER than previous value
        return value + romanToInteger(tail, value)
    else:
        # present value LESS than previous value
        return -value + romanToInteger(tail, value)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    while True:
        number = input("Enter the ROMAN number: ")
        if checkEntry(number):
            break

    # CONVERSION "STRING" -> [LIST reversed]
    number_list = list(number.upper())
    number_list.reverse()
    integer = romanToInteger(number_list, 0)

    # Displaying the RESULT
    print("The ROMAN NUMBER \"{}\" is equivalent to the INTEGER \"{}\"".format(
        number, integer))


if __name__ == "__main__":
    main()
