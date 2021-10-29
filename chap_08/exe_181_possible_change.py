"""
Create a program that determines whether or not it is possible to construct a particular total
using a specific number of coins.

For example:
it is possible to have a total of $1.00 using four coins if they are all quarters.

However, there is no way to have a total of $1.00 using 5 coins.
Yet it is possible to have $1.00 using 6 coins by using 3 quarters, 2 dimes and a nickel.

Similarly, a total of $1.25 can be formed using 5 coins or 8 coins,
but a total of $1.25 cannot be formed using 4, 6 or 7 coins.

Your program should read both the dollar amount and the number of coins from the user.

Then it should display a clear message indicating whether or not the entered dollar amount
can be formed using the number of coins indicated.

Assume the existence of quarters, dimes, nickels and pennies when completing this problem.

Your solution must use recursion. It cannot contain any loops.
"""

# IMPORT combinations_with_replacement module (from ITERTOOLS)
from itertools import combinations_with_replacement


# START Definition of the FUNCTIONS


def checkEntry(number):     # possible evolution -> import module
    return True


# possible evolution -> RECURSIVE FUNCTION
def checkNumberCoins(amount, coins, num_coins):
    # LIST of COMBINATIONS WITH REPLACEMENT
    all_combinations = list(combinations_with_replacement(coins, num_coins))
    # Check of the presence of combinations
    # having the sum that matches with the entered amount by the user
    for combination in all_combinations:
        # Check with positive result
        if round(sum(combination), 2) == amount:
            return combination
    # Check with negative result
    return ("")


# END Definition of the FUNCTIONS


# START MAIN PROGRAM
def main():

    # LIST of COINS
    COINS = [0.25, 0.10, 0.05, 0.01]

    # Acquisition and Control of the DATA entered by the USER
    entry = True
    while entry:
        amount = input("Enter the dollar amount: ")
        num_coins = input("Enter the number of coins: ")
        if checkEntry(amount) and checkEntry(num_coins):
            entry = False

    # Conversion STR -> INT/FLOAT
    amount = float(amount)
    num_coins = int(num_coins)

    # Generation of any COMBINATION of COINS
    combination = checkNumberCoins(amount, COINS, num_coins)

    # Displaying the RESULTS
    if len(combination) == 0:
        print("There are NO COMBINATIONS of coins that form the entered AMOUNT ($ {}).".format(amount))
    else:
        print("The COINS COMBINATION that forms the entered AMOUNT ($ {}) is".format(
            amount), combination)


if __name__ == "__main__":
    main()
