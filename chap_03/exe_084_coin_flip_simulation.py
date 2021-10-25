"""
What's the minimum number of times you have to flip a coin
before you can have three consecutive flips that result in the same outcome
(either all three are heads or all three are tails)?
What's the maximum number of flips that might be needed?
How many flips are needed on average?
In this exercise we will explore these questions by creating a program
that simulates several series of coin flips.

Create a program that uses a random number generator to simulate flipping a coin several times.
The simulated coin should be fair,
meaning that the probability of heads is equal to the probability of tails.
Your program should flip simulated coins until either 3 consecutive heads of 3 consecutive tails occur.
Display an H each time the outcome is heads,
and a T each time the outcome is tails,
with all of the outcomes for one simulation on the same line.
Then display the number of flips that were needed to reach 3 consecutive occurrences of the same outcome.
When your program is run it should perform the simulation 10 times and report the average number of flips needed.
Sample output is shown below:

H T T T (4 flips)
H H T T H T H T T H H T H T T H T T T (19 flips)
T T T (3 flips)
T H H H (4 flips)
H H H (3 flips)
T H T T H T H H T T H H T H T H H H (18 flips)
H T T H H H (6 flips)
T H T T T (5 flips)
T T H T T H T H T H H H (12 flips)
T H T T T (5 flips)

On average, 7.9 flips were needed.
"""

# IMPORT module RANDOM
import random


# Declaration of VARIABLES
SIMULATIONS = 10
MIN_VALUE = 1
MAX_VALUE = 100
total_flips = 0


# Displaying the HEADER
print("************************* COIN FLIP SIMULATION *************************\n")


# COIN FLIP SIMULATIONS
for i in range(SIMULATIONS):
    flips = 0
    heads = 0
    tails = 0
    while (heads != 3 and tails != 3):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        if value % 2 == 0:
            print("H", end = " ")
            flips += 1
            heads +=1
            tails = 0
        else:
            print("T", end = " ")
            flips += 1
            tails += 1
            heads = 0
    print("(" + str(flips) + " flips)")
    total_flips += flips
    average_flips = total_flips / SIMULATIONS


# Displaying the RESULTS
print("\nOn AVERAGE %.1f" % average_flips + " FLIPS were needed.")
print("************************************************************************")