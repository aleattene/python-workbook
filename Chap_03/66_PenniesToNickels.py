"""
The program receives from the USER the PRICE of some ITEMS (in PENNIES)
and returns (displaying it) the TOTAL COST for the CONSUMER
 depending on whether the payment is made:
- by CREDIT or DEBIT CARD (in this case the total cost is NOT rounded to the nearest NICKEL).
- by CASH (in this case the total cost is ROUNDED to the nearest NICKEL).
"""

# START Definition of FUNCTION


def valutaIntegerPositive(numero):
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


# END Definition of FUNCTION


# Declaration of VARIABLES
totalPennies = 0


# Acquisition and Control of the DATA entered by the USER
pennies = input(
    "Enter the PRICE (pennies) of the ITEM or press ENTER (blank line) to QUIT: ")
penniesValidated = valutaIntegerPositive(pennies)

while pennies != "":
    if penniesValidated:
        totalPennies += int(pennies)
        pennies = input(
            "Enter the PRICE (pennies) of the ITEM or press ENTER (blank line) to QUIT: ")
        penniesValidated = valutaIntegerPositive(pennies)
    else:
        print("Incorrect entry. Try again.")
        pennies = input(
            "Enter the PRICE (pennies) of the ITEM or press ENTER (blank line) to QUIT: ")
        penniesValidated = valutaIntegerPositive(pennies)


# TOTAL COST computing
remainder = totalPennies % 5

if remainder < 2.5:
    totalPenniesCash = totalPennies - remainder
    totalNickelsCash = totalPenniesCash // 5
else:
    totalPenniesCash = totalPennies + (5 - remainder)
    totalNickelsCash = totalPenniesCash // 5


# Displaying the RESULTS
print("Payment by CREDIT or DEBIT CARD -> Total COST of the ITEMS: " +
      str(totalPennies) + " pennies")
print("Payment by CASH -> Total COST of the ITEMS: " + str(totalPenniesCash) + " pennies or " +
      str(totalNickelsCash) + " nickels")
