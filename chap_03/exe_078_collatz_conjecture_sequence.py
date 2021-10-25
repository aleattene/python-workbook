"""
The program receives an INTEGER POSITIVE NUMBER from the user
and displays the so-called COLLATZ CONJECTURE SEQUENCE.
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
