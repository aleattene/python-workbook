"""
The program SIMULATES COIN FLIPS 
and returns the AVERAGE number of FLIPS, 
needed to have THREE CONSECUTIVE HEADS or three consecutive TAILS.
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