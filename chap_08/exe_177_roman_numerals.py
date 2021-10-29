"""
As the name implies, Roman numerals were developed in ancient Rome.

Even after the Roman empire fell, its numerals continued to be widely used in Europe until the late middle ages,
and its numerals are still used in limited circumstances today.

Roman numerals are constructed from the letters M, D, C, L, X, V and
I which represent 1000, 500, 100, 50, 10, 5 and 1 respectively.
The numerals are generally written from largest value to smallest value.
When this occurs the value of the number is the sum of the values of all of its numerals.

If a smaller value precedes a larger value then
the smaller value is subtracted from the larger value that it immediately precedes, and
that difference is added to the value of the number.

Create a recursive function that converts a Roman numeral to an integer.

Your function should process one or two characters at the beginning of the string, and then
call itself recursively on all of the unprocessed characters.
Use an empty string, which has the value 0, for the base case.

In addition, write a main program that reads a Roman numeral from the user and displays its value.

You can assume that the value entered by the user is valid.

Your program does not need to do any error checking.
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
