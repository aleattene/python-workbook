"""
The program receives TWO POSITIVE INTEGER numbers from the USER 
and returns (displaying it) their GREATEST COMMON DIVISOR.
"""


# START Definition of FUNCTIONS


def valutaIntegerPositive(numero):
    if numero.isdigit():
        if int(numero) > 0:
            return True
    return False


def computesGreatestCommonDivisor(number_1, number_2):
    gcd = number_1
    while (number_1 % gcd) != 0 or (number_2 % gcd) != 0:
        gcd -=1
    return gcd 


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
number_1 = input("Enter the FIRST POSITIVE INTEGER NUMBER: ")
number_1_validated = valutaIntegerPositive(number_1)
number_2 = input("Enter the SECOND POSITIVE INTEGER NUMBER: ")
number_2_validated = valutaIntegerPositive(number_2)

while not(number_1_validated and number_2_validated):
    print("Incorrect entry. Try again.")
    number_1 = input("Enter the FIRST POSITIVE INTEGER NUMBER: ")
    number_1_validated = valutaIntegerPositive(number_1)
    number_2 = input("Enter the SECOND POSITIVE INTEGER NUMBER: ")
    number_2_validated = valutaIntegerPositive(number_2)


# Conversion STR -> INT
number_1 = int(number_1)
number_2 = int(number_2)


# Computing the Greater Common Divisor of number_1 and number_2
gcd = computesGreatestCommonDivisor(number_1,number_2)


# Displaying the RESULT
print("The GREATEST COMMON DIVISOR of " + str(number_1) + " and " + \
    str(number_2) + " is \"" + str(gcd) + "\".")
