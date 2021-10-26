"""
Words like first, second and third are referred to as ordinal numbers.
In this exercise, you will write a function that takes an integer as its only parameter and
returns a string containing the appropriate English ordinal number as its only result.
Your function must handle the integers between 1 and 12 (inclusive).
It should return an empty string if the function is called with an argument outside of this range.
Include a main program that demonstrates your function
by displaying each integer from 1 to 12 and its ordinal number.
Your main program should only run when your file has not been imported into another program.
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
