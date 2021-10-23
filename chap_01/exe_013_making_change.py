"""
Consider the software that runs on a self-checkout machine.
One task that it must be able to perform is to determine
how much change to provide when the shopper pays for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an integer.
Then your program should compute and display the denominations of the coins
that should be used to give that amount of change to the shopper.
The change should be given using as few coins as possible.
Assume that the machine is loaded with pennies, nickels, dimes, quarters, loonies and toonies.
"""

# Declaration of VARIABLES
toonies = 0     # 1 toonie = 200 cents = 2 $ CANADIANS
loonies = 0     # 1 loonie = 100 cents = 1 $ CANADIAN
quarters = 0    # 1 quarter = 25 cents = 1/4 di $ CANADIAN
dimes = 0       # 1 dime = 10 cents = 1/10 di $ CANADIAN
nickels = 0     # 1 nickel = 5 cents = 1/20 di $ CANADIAN
pennies = 0     # 1 penny = 1 cent = 1/100 di $ CANADIAN


# Acquisition and Control of the DATA entered by the USER
cents = input("Enter the quantity (CENTS) to CHANGE: ")

while not(cents.isdigit() and cents != "0"):
    print("Incorrect entry. Try again.")
    cents = input("Enter the quantity (CENTS) to CHANGE: ")


# Conversion STR -> INT
cents = int(cents)

# Computing RESULTS (toonies, loonies, quarters, dimes, nickels, pennies)
if cents >= 200:
    toonies = cents // 200
    cents = cents % 200
if cents >= 100:
    loonies = cents // 100
    cents = cents % 100
if cents >= 25:
    quarters = cents // 25
    cents = cents % 25
if cents >= 10:
    dimes = cents // 10
    cents = cents % 10
if cents >= 5:
    nickels = cents // 5
    cents = cents % 5

pennies = cents

# Displaying the RESULTS
print("RESULTS:")
print(f'- Toonies = {toonies}')
print(f'- Loonies = {loonies}')
print(f'- Quarters = {quarters}')
print(f'- Dimes = {dimes}')
print(f'- Nickels = {nickels}')
print(f'- Pennies = {pennies}')
