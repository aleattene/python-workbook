"""
The prime factorization of an integer, n, can be determined using the following steps:

Initialize factor to 2 While factor is less than or equal to n
do If n is evenly divisible by factor
then Conclude that factor is a factor of n
Divide n by factor using floor division Else Increase factor by 1

Write a program that reads an integer from the user.
If the value entered by the user is less than 2
then your program should display an appropriate error message.

Otherwise your program should display the prime numbers
that can be multiplied together to compute n,
with one factor appearing on each line.

For example:

Enter an integer (2 or greater): 72 The prime factors of 72 are:
 2
 2
 2
 3
 3
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
