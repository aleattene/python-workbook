"""
The program GENERATES 6 RANDOM NUMBERS for a LOTTERY 
(from 1 to 49 and without duplicates) 
and DISPLAYING them in ASCENDING ORDER.
"""

# IMPORT RANDOM module
import random


# START Definition of the FUNCTIONS


def generateNumber(start, stop):
    number = random.randint(start, stop)   # beetween 1 and 49
    return number


def generateWinningNumbers(n, start, stop):
    winning_numbers = []
    while len(winning_numbers) < n:
        number = generateNumber(start, stop)
        if number not in winning_numbers:
            winning_numbers.append(number)
    return winning_numbers


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Initialization of the VARIABLES / CONSTANTS
    NUMBERS_LOTTERY = 6
    START_NUMBER = 1
    STOP_NUMBER = 49

    # Generation of the WINNING NUMBERS
    winning_numbers = generateWinningNumbers(
        NUMBERS_LOTTERY, START_NUMBER, STOP_NUMBER)
    winning_numbers.sort()

    # Displaying the WINNING NUMBERS in ASCENDING ORDER
    print("WINNING NUMBERS -> ", end="")
    for number in winning_numbers:
        print(str(number) + " ", end="")


if __name__ == "__main__":
    main()
