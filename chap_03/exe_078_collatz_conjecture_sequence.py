"""
Consider a sequence of integers that is constructed in the following manner:

Start with any positive integer as the only term in the sequence
While the last term in the sequence is not equal to 1 do
If the last term is even then
Add another term to the sequence by dividing the last term by 2 using floor division
Else Add another term to the sequence by multiplying the last term by 3 and adding 1

The Collatz conjecture states that this sequence will eventually end
with one when it begins with any positive integer.
Although this conjecture has never been proved,
it appears to be true.

Create a program that reads an integer, n, from the user and
reports all of the values in the sequence starting with n
and ending with one.

Your program should allow the user to continue entering new n values
(and your program should continue displaying the sequences)
until the user enters a value for n that is less than or equal to zero.

The Collatz conjecture is an example of an open problem in mathematics.
While many people have tried to prove that it is true,
no one has been able to do so.

Information on other open problems in mathematics can be found on the Internet.
"""


# START Definition of FUNCTIONS


def valutaInteger(numero):
    if len(numero) > 1:
        if numero.isdigit() or \
                (numero[0] == "-" and numero[1] != "0" and numero[1:].isdigit()):
            return True
    else:
        if numero.isdigit():
            return True
    return False


# END Definition of FUNCTIONS


# VARIABLE declaration
integer = "1"


# Acquisition and Control of the DATA entered by the USER
while int(integer) > 0:
    integer = input("Enter the INTEGER NUMBER (less or equal to ZERO to QUIT): ")
    integer_validated = valutaInteger(integer)

    while not(integer_validated):
        print("Incorrect entry. Try again.")
        integer = input("Enter the INTEGER NUMBER (less or equal to ZERO to QUIT): ")
        integer_validated = valutaInteger(integer)

    last_term = int(integer)

    # COLLATZ CONJECTURE SEQUENCE (generation and displaying)
    if last_term > 0:
        print("*** COLLATZ CONJECTUR SEQUENCE***")
        print("%16s" % last_term)
        while last_term != 1:
            if last_term % 2 == 0:
                last_term = last_term // 2
            else:
                last_term = (last_term * 3) + 1
            print("%16s" % last_term)
        print("*********************************")
