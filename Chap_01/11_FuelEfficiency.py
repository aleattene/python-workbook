"""
The program receives in INPUT from the USER a quantity of fuel efficiency expressed in MPG
and converts it to L/100km.
Remember that:
- MPG = miles-per-gallon (United States units)
- L/100km = liter-per-hundred kilometers (Canadian units)
- L/100km = 235.214583 / MPG
"""

# Start Definition of FUNCTIONS


def valutaFloat(mpg):
    countPoints = 0
    for char in mpg:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and mpg != ".":
        if isinstance(float(mpg), float):
            return True
    else:
        return False


# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
mpg = input("Enter the FUEL EFFICIENCY (MPG) to convert (L/100km): ")

numberFloat = valutaFloat(mpg)  # function call

while not(mpg.isdigit() and mpg != "0") and not(numberFloat):
    print("Incorrect entry. Try again.")
    mpg = input("Enter the FUEL EFFICIENCY (MPG) to convert (L/100km): ")
    numberFloat = valutaFloat(mpg)  # function call

# Computing MPG -> LITRI/100km
mpg = float(mpg)     # conversion string -> float
literHundredKm = 235.214583 / mpg

# Displaying the RESULT
print("RESULT CONVERSION FUEL EFFICIENCY -> %.2f" % mpg + " MPG (American Units) = %.2f" % literHundredKm
      + " L/100Km (Canadian Units)")
