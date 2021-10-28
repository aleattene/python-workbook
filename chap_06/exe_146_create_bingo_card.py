"""
A Bingo card consists of 5 columns of 5 numbers which are labelled with the letters B, I, N, G and O.

There are 15 numbers that can appear under each letter.

In particular, the numbers that can appear under the B range from 1 to 15,
the numbers that can appear under the I range from 16 to 30,
the numbers that can appear under the N range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary.

The keys will be the letters B, I, N, G and O.
The values will be the lists of five numbers that appear under each letter.
Write a second function that displays the Bingo card with the columns labelled appropriately.

Use these functions to write a program that displays a random Bingo card.

Ensure that the main program only runs when the file containing your solution
has not been imported into another program.
"""

# IMPORT RANDOM module
import random


# START Definition of the FUNCTIONS


def createBingoCard():
    # Dictionary of the BINGO CARD
    bingo_card_dict = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []
    }
    # Numbers for EACH COLUMN of the bingo card
    NUMBERS_COLUMN = 5
    # Range of FIRST COLUMN NUMBERS
    start_numbers = 1
    end_numbers = 15
    i = -15
    for letter in bingo_card_dict:
        # INCREASE of the RANGE of COLUMN NUMBERS
        i += 15
        for number in range(NUMBERS_COLUMN):
            number = random.randint(start_numbers + i, end_numbers + i)
            # Adding number to dictionary (in the specific key list)
            bingo_card_dict[letter].append(number)
    return bingo_card_dict


def displayBingoCard(bingo_card):
    # LABELS for HEADER bingo card -> dictionary KEYS
    print("-" * 46)
    print("|    ", end="")
    for key in bingo_card:
        print("{:1s}".format(key), end="   |    ")
    print("")
    print("-" * 46)
    # NUMBERS of the EACH COLUMN of the BINGO CARD
    for i in range(len(bingo_card[key])):
        print("|   ", end="")
        for key in bingo_card:
            print("{:2d}".format(bingo_card[key][i]), end="   |   ")
        print("")
    # FOOTER bingo card
    print("-" * 46)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # BINGO CARD creation
    bingo_card = createBingoCard()

    # BINGO CARD DISPLAY
    displayBingoCard(bingo_card)


if __name__ == "__main__":
    main()
