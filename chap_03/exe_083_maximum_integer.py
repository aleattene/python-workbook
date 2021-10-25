"""
The program RANDOMLY GENERATES 100 INTEGER NUMBERS 
and returns BOTH the MAXIMUM detected VALUE 
and the NUMBER of TIMES in which this VALU was UPDATED.
"""

# IMPORT module RANDOM
import random


# Declaration of VARIABLES
max_value = 0
update = 0


# Computing of the MAXIMUM VALUE between 100 RANDOMLY INTEGERS generated
for i in range(100):
    value = random.randint(1, 100)
    if value > max_value:
        max_value = value
        update += 1
        print(value, "<-- Maximum VALUE UPDATED")
        continue
    print(value)


# Displaying the RESULTS
print("The MAXIMUM VALUE found was " + str(max_value))
print("The MAXIMUM VALUE was UPDATED " + str(update) + " times")
