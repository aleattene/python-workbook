""" 
The Program receives from the USER an INTEGER (consisting of "n" DIGITS)
and calculates the SUM of the "n" DIGITS that make up the number itself.
"""

# START Definition of FUNCTIONS


def valutaInteger(numero):
    if numero.isdigit():
        return True
    return False


def sumInteger(number):
    sumInteger = 0
    for char in number:
        sumInteger = sumInteger + int(char)
    return sumInteger


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
number = input("Enter the INTEGER: ")
numberValidated = valutaInteger(number)

while not(numberValidated):
    print("Incorrect entry. Try again.")
    number = input("Enter the INTEGER: ")
    numberValidated = valutaInteger(number)


# Computing of the SUM of INTEGER DIGITS
sumInteger = sumInteger(number)

# Displaying the RESULT
print("SUM INTEGER = " + str(sumInteger))
