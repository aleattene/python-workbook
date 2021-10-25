"""
The program DISPLAYS the ANSWERS for the FIRST 100 NUMBERS
in the FIZZ-BUZZ game.
"""


# Declaration of VARIABLES
number = 1


# Displaying the HEADER
print("*****************************")
print("|      List of ANSWERS      |")
print("| for the FIRST 100 NUMBERS |")
print("|   of the FIZZ-BUZZ game   |")
print("*****************************")


# Computing the ANSWERS for the FIRST 100 NUMBERS (FIZZ-BUZZ game)
in the FIZZ-BUZZ game.
while number <= 100:
    if number % 3 == 0:                             # divisible by 3
        if number % 5 == 0:                         # divisible (by 3) and by 5
            answer = "FIZZ  BUZZ"
            # Displaying the PROGRESSIVE RESULT
            print("|%18s" % answer + "%9s|" % "")
        else:                                       # divisible only by 3
            answer = "FIZZ"
            # Displaying the PROGRESSIVE RESULT
            print("|%15s" % answer + "%12s|" % "")
    else:                                           # not divisibile by 3 or by 5
        if number < 10:
            answer = "0" + str(number)
        else:
            answer = str(number)
        # Displaying the PROGRESSIVE RESULT
        print("|%14s" % answer + "%13s|" % "")
    number += 1


# Displaying the FOOTER
print("*****************************")