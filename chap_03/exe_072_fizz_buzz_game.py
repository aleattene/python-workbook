"""
Fizz-Buzz is a game that is sometimes played by children
to help them learn about division.
The players are commonly arranged in a circle so that the game can progress
from player to player continually.
The starting player begins by saying one, and then play passes to the player to the left.
Each subsequent player is responsible
for the next integer in sequence before play passes to the following player.

On a player’s turn they must either say their number or one of following substitutions:
- if the player’s number is divisible by 3 then the player says fizz instead of their number,
- if the player’s number is divisible by 5 then the player says buzz instead of their number.

A player must say both fizz and buzz for numbers that are divisible by both 3 and 5.
Any player that fails to perform the correct substitution or
hesitates before answering is eliminated from the game.
The last player remaining is the winner.

Write a program that displays the answers for the first 100 numbers in the Fizz- Buzz game.
Each answer should be displayed on its own line.
"""


# Declaration of VARIABLES
number = 1


# Displaying the HEADER
print("*****************************")
print("|      List of ANSWERS      |")
print("| for the FIRST 100 NUMBERS |")
print("|   of the FIZZ-BUZZ game   |")
print("*****************************")


# Computing the ANSWERS for the FIRST 100 NUMBERS (FIZZ-BUZZ game) in the FIZZ-BUZZ game.
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
