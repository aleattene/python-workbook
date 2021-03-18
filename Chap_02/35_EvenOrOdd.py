"""
The Program receives from the USER an INTEGER 
and displays if it’s an ODD or EVEN number.
"""

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def evenOrOdd(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
numberInt = input("Enter an INTEGER number: ")
numberIntPositive = valutaIntPositive(numberInt)

while not(numberIntPositive):
    print("Incorrect entry. Try again.")
    numberInt = input("Enter an INTEGER number: ")
    numberIntPositive = valutaIntPositive(numberInt)


# Conversion STR -> INT
numberInt = int(numberInt)


# Valuation EVEN or ODD number
typeNumber = evenOrOdd(numberInt)


# Displaying the RESULT (formatted)
print("The NUMBER " + str(numberInt) + " is " + typeNumber)
