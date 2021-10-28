"""
While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors.
The amount being paid normally appears on a cheque twice, with one occurrence written using digits, and
the other occurrence written using English words.

Repeating the amount in two different forms
makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.
In this exercise, your task is to create a function that
takes an integer between 0 and 999 as its only parameter, and
returns a string containing the English words for that number.

For example, if the parameter to the function is 142 then your function should return “one hundred forty two”.

Use one or more dictionaries to implement your solution rather than large if/elif/else constructs.
Include a main program that reads an integer from the user and displays its value in English words.
"""


# START Definition of the FUNCTIONS


def checkEntry(values_string):
    if values_string.isdigit():
        if 0 <= int(values_string) <= 999:
            return True


def digitsToWords(amount_digits):
    # AMOUNT written in words
    amount_words = ""
    # DICTIONARIES (units, ten_to_nineteen, tens ad hundreds)
    units = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }
    ten_to_nineteen = {
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen"
    }
    tens = {
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety",
    }
    hundreds = {
        "1": "one hundred",
        "2": "two hundred",
        "3": "three hundred",
        "4": "four hundred",
        "5": "five hundred",
        "6": "six hundred",
        "7": "seven hundred",
        "8": "eight hundred",
        "9": "nine hundred",
    }
    # NUMBERS: 100 -> 999
    if 100 <= amount_digits <= 999:
        amount_words += hundreds[str(amount_digits)[0]] + " "
        amount_digits = int(str(amount_digits)[1:])
    # NUMBERS: 20 -> 99
    if 20 <= amount_digits <= 99:
        amount_words += tens[str(amount_digits)[0]] + " "
        amount_digits = int(str(amount_digits)[1])
    # NUMBERS: 10 -> 19
    if 10 <= amount_digits <= 19:
        amount_words += ten_to_nineteen[str(amount_digits)]
    # NUMBERS: 0 -> 9
    if 0 <= amount_digits <= 9:
        amount_words += units[str(amount_digits)]
    return amount_words


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    while True:
        amount_digits = input(
            "Enter the AMOUNT (in DIGITS) written on the CHEQUE (between 0 and 999): ")
        if checkEntry(amount_digits):
            break
        else:
            continue

    # STRING TESTING
    # amount_digits = "2"
    # amount_digits = "14"
    # amount_digits = "142"

    # AMOUNT conversion -> from DIGITS to WORDS
    amount_words = digitsToWords(int(amount_digits))

    # Displaying the AMOUNT written on the CHEQUE both in DIGITS and in WORDS.
    print("AMOUNTS written on the CHEQUE -> ({}) and \"{}\".".format(amount_digits, amount_words))


if __name__ == "__main__":
    main()
