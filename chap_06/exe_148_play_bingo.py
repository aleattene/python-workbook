"""
In this exercise you will write a program that simulates a game of Bingo for a single card.

Begin by generating a list of all of the valid Bingo calls (B1 through O75).

Once the list has been created you can randomize the order of its elements
by calling the shuffle function in the random module.

Then your program should consume calls out of the list and cross out numbers on the card
until the card contains a winning line.

Simulate 1,000 games and report the minimum, maximum and average number of calls
that must be made before the card wins.

You may find it helpful to import your solutions to Exercises "Create a Bingo Card" and
"Checking for a winning Card" when completing this exercise.
"""

# IMPORT RANDOM and COPY modules
import random
import copy


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


def checkWinningCard(call, bingo_card):  # FUNCTION modified (list vs string)
    # Crossing out of the winning numbers (Warning -> Edit dictionary passed as parameter)
    for key in bingo_card:
        for i in range(len(bingo_card[key])):
            if bingo_card[key][i] == int(call[1:]):
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


def generateBingoCalls():
    # LIST of the VALID BINGO CALLS
    bingo_calls = []
    for i in range(1, 76):
        # FIRST COLUMN
        if i <= 15:
            bingo_calls.append("B" + str(i))
        # SECOND COLUMN
        elif 16 <= i <= 30:
            bingo_calls.append("I" + str(i))
        # THIRD COLUMN
        elif 31 <= i <= 45:
            bingo_calls.append("N" + str(i))
        # FOURTH COLUMN
        elif 46 <= i <= 60:
            bingo_calls.append("G" + str(i))
        # FIFTH COLUMN
        else:  # 61 <= i <= 75:
            bingo_calls.append("O" + str(i))
    return bingo_calls


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # SINGLE BINGO CARD creation
    bingo_card_original = createBingoCard()

    # SINGLE BINGO CARD display
    displayBingoCard(bingo_card_original)

    # Declaration of VARIABLES / CONSTANTS
    minimum = 75
    maximum = 1
    count = 0
    total = 0
    SIMULATIONS = 1000
    # START SIMULATIONS (possible evolution -> function simulate)
    for simulate in range(SIMULATIONS):
        # DEEP COPY BINGO CARD
        bingo_card = copy.deepcopy(bingo_card_original)
        # VALID CALLS creation
        valid_calls = generateBingoCalls()
        # Randomizing the order of the valid calls
        random.shuffle(valid_calls)
        # Calls count
        count = 0
        # Start Calls
        for call in valid_calls:
            result = checkWinningCard(call, bingo_card)
            count += 1
            if result:
                break
        total += count
        # Counting of minimum necessary calls
        if count < minimum:
            minimum = count
        # Counting of maximum necessary calls
        if count > maximum:
            maximum = count
    # Counting of average necessary calls
    average = total // SIMULATIONS

    # Displaying the RESULTS
    print("STATISTICS of the BINGO GAME")
    print("Number of SIMULATIONS = {}".format(SIMULATIONS))
    print("The MINIMUM NUMBER of CALLS that must be made before the card WINS are {}".format(
        minimum))
    print("The MAXIMUM NUMBER of CALLS that must be made before the card WINS are {}".format(
        maximum))
    print("The AVERAGE NUMBER of CALLS that must be made before the card WINS are {}".format(
        average))


if __name__ == "__main__":
    main()
