"""
The program receives an INTEGER number (greater or equal to 2) from the USER 
and returns (displaying them) its PRIME FACTORS.
"""


# START Definition of the FUNCTION


def valutaentry(numero):
    if numero.isdigit():
        if int(numero) >= 2:
            return True
    return False


# END Definition of the FUNCTION


# Acquisition and Control of the DATA entered by the USER
number = input("Enter the POSITIVE INTEGER NUMBER: ")
number_validated = valutaentry(number)

while not(number_validated):
    print("Incorrect entry. Try again.")
    number = input("Enter the POSITIVE INTEGER NUMBER: ")
    number_validated = valutaentry(number)


# HEADER display
print("The PRIME FACTORS of " + str(number) + " are: ", end=" ")

# PRIME FACTORS (computing and displaying)
number = int(number)
factor = 2

while factor <= number:
    if number % factor == 0:
        number = number // factor
        print(factor, end="  ")
    else:
        factor += 1
