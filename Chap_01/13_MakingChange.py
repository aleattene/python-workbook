"""
The Program receives in INPUT from the USER a certain number
of Cents of Dollar (Canadian) and displays the EXCHANGE
with COINS as large as possible.
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
    toonies = int(cents / 200)
    cents = cents % 200
if cents >= 100:
    loonies = int(cents / 100)
    cents = cents % 100
if cents >= 25:
    quarters = int(cents / 25)
    cents = cents % 25
if cents >= 10:
    dimes = int(cents / 10)
    cents = cents % 10
if cents >= 5:
    nickels = int(cents / 5)
    cents = cents % 5

pennies = cents

# Displaying the RESULTS
print("RESULTS:")
print("- Toonies = %i" % toonies)
print("- Loonies = %i" % loonies)
print("- Quarters = %i" % quarters)
print("- Dimes = %i" % dimes)
print("- Nickels = %i" % nickels)
print("- Pennies = %i" % pennies)
