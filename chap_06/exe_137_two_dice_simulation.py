"""
In this exercise you will simulate 1,000 rolls of two dice.
Begin by writing a function that simulates rolling a pair of six-sided dice.
Your function will not take any parameters.
It will return the total that was rolled on two dice as its only result.
Write a main program that uses your function to simulate rolling two six-sided dice 1,000 times.
As your program runs, it should count the number of times that each total occurs.
Then it should display a table that summarizes this data.
Express the frequency for each total as a percentage of the number of rolls performed.
Your program should also display the percentage expected by probability theory for each total.
To summarize, the program should SIMULATES 1000 ROLLS of TWO DICE and displays:
- the TOTAL that was OBTAINED with the two dice
- the PERCENTAGE of the NUMBER of TIMES when one total was obtained
- the percentage EXPECTED by PROBABILITY THEORY for each total obtained
"""

# Import RANDOM module
import random


# START Definition of the FUNCTION


def rollsTwoDice():
    NUMBER_ROLLS = 1000
    SIDES_DICE = 6
    NUM_DICE = 2
    POSSIBLE_ROLLS = SIDES_DICE ** NUM_DICE
    # DICTIONARY (ALL ROLLS of DICE)
    summary_rolls = {}
    # Execution of 1000 DICE ROLLS
    for i in range(NUMBER_ROLLS):
        total = 0
        # SINGLE ROLL of the dice
        for die in range(NUM_DICE):
            die_n = random.randint(1, SIDES_DICE)
            total += die_n
        if total in summary_rolls:
            # UPDATE VALUE (count) in DICTIONARY
            summary_rolls[total][0] += 1/(NUMBER_ROLLS/100)
        else:
            # NEW INSERT (item) in DICTIONARY
            summary_rolls[total] = [1/(NUMBER_ROLLS/100)]
            # PROBABILITY THEORY
            if total <= (SIDES_DICE * NUM_DICE) / 2:
                summary_rolls[total].append((total-1)/POSSIBLE_ROLLS*100)
            else:
                summary_rolls[total].append(
                    ((SIDES_DICE - (total-(SIDES_DICE+1)))/POSSIBLE_ROLLS)*100)
    return summary_rolls


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # DICTIONARY (ALL ROLLS of DICE)
    summary_rolls = rollsTwoDice()

    # Displaying the RESULTS
    print("TOTAL     SIMULATED %   " + "  EXPECTED %")
    for key in sorted(summary_rolls):
        print("{:3d}         {:5.2f}          {:5.2f}".format(
            key, summary_rolls[key][0], summary_rolls[key][1]))


if __name__ == "__main__":
    main()
