"""
The program receives from the USER the MONEY DEPOSITED 
in one savings account and displays the amount in the same account
after 1, 2 and 3 years, based on a compound interest rate of 4% annual.
"""

# Start Definition of FUNCTIONS


def calcolaInteresse(amount):
    TAX_INTEREST = 1.04          # compound interest 4% annual
    return amount * TAX_INTEREST


def valutaFloat(amount):
    countPoints = 0
    for char in amount:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and amount != ".":
        if isinstance(float(amount), float):
            return True
    else:
        return False

# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
amount = input(
    "Enter the amount of MONEY deposited in the savings account (€): ")
numberFloat = valutaFloat(amount)

while not(amount.isdigit()) and not(numberFloat):
    print("Incorrect entry. Try again by entering a new amount")
    amount = input(
        "Enter the amount of MONEY deposited in the savings account (€): ")
    numberFloat = valutaFloat(amount)

# Computing of ANNUAL INTERESTS
amount = float(amount)     # conversion string -> float
amountYears01 = calcolaInteresse(amount)
amountYears02 = calcolaInteresse(amountYears01)
amountYears03 = calcolaInteresse(amountYears02)

# Displaying the RESULTS
print("Amount of money deposited at the end of the first year € %.2f" %
      amountYears01)
print("Amount of money deposited at the end of the second year € %.2f" %
      amountYears02)
print("Amount of money deposited at the end of the third year € %.2f" %
      amountYears03)
