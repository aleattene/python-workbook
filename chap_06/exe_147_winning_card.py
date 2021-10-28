"""
The program CREATES and displays a BINGO CARD.
After that, asks the USER to ENTER the combination of the WINNING NUMBERS
and check WHETHER this BINGO CARD is WINNING or NOT.
"""

# IMPORT RANDOM module
import random


# START Definition of the FUNCTIONS


def createBingoCard():  # possible evolution -> IMPORT FUNCTION from 146
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


def displayBingoCard(bingo_card):  # possible evolution -> IMPORT FUNCTION from 146
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


def checkWinningCard(winning_numbers, bingo_card):
    # Winning NUMBERS combination
    numbers = winning_numbers.split()
    # Conversion [STR] -> [INT]
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    # Crossing out of the winning numbers (Warning -> Edit Original Dictionary)
    for key in bingo_card:
        for i in range(len(bingo_card[key])):
            if bingo_card[key][i] in numbers:
                bingo_card[key][i] = 0
    # Check if the COLUMN of the BINGO CARD is WINNING
    for key in bingo_card:
        if sum(bingo_card[key]) == 0:
            return True
    # Check if the LINE of the BINGO CARD is WINNING
    for i in range(len(bingo_card[key])):
        total = 0
        for key in bingo_card:
            total += bingo_card[key][i]
        if total == 0:
            return True
    # Check if the DIAGONALS of the BINGO CARD is WINNING
    total_sx = 0
    total_dx = 0
    i_sx = 0
    i_dx = (len(bingo_card)-1)
    for key in bingo_card:
        # LEFT diagonal
        total_sx += bingo_card[key][i_sx]
        # RIGHT diagonal
        total_dx += bingo_card[key][i_dx]
        i_sx += 1
        i_dx -= 1
    if total_sx == 0 or total_dx == 0:
        return True
    return False


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # BINGO CARD creation
    bingo_card = createBingoCard()

    # BINGO CARD DISPLAY
    displayBingoCard(bingo_card)

    # Acquisition of DATA entered by the USER
    winning_numbers = input(
        "Enter the WINNING NUMBERS (separated by a whitespace): ")

    # Displaying the RESULTS
    result = checkWinningCard(winning_numbers, bingo_card)
    displayBingoCard(bingo_card)
    if result:
        print("Congratulations. YOU WON.")
    else:
        print("I’m sorry. YOU didn’t win.")


if __name__ == "__main__":
    main()
