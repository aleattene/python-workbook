"""
The program receives THREE VALUES from the USER
and returns (displaying it) their MEDIAN.
"""


# START Definition of the FUNCTIONS


def integerToOrdinal(number):
    ordinal_numbers = {
        "1": "FIRST",
        "2": "SECOND",
        "3": "THIRD",
        "4": "FOURTH",
        "5": "FIFTH",
        "6": "SIXTH",
        "7": "SEVENTH",
        "8": "EIGHTH",
        "9": "NINTH",
        "10": "TENTH",
        "11": "ELEVENTH",
        "12": "TWELFTH"
    }
    if number in ordinal_numbers.keys():
        return ordinal_numbers[number]
    else:
        return "OUT of RANGE"


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the NUMBER (from 1 to 12): ")

    # MEDIAN computing
    ordinal = integerToOrdinal(number)

    # Displaying the RESULT
    print("The NUMBER {0} corresponds at the ordinal number {1}".format(
        number, ordinal))


if __name__ == "__main__":
    main()
