"""
A parity bit is a simple mechanism for detecting errors in data transmitted
over an unreliable connection such as a telephone line.
The basic idea is that an additional bit is transmitted
after each group of 8 bits so that a single bit error in the transmission can be detected.
Parity bits can be computed for either even parity or odd parity.
If even parity is selected then the parity bit that is transmitted
is chosen so that the total number of one bits transmitted
(8 bits of data plus the parity bit) is even.
When odd parity is selected the parity bit
is chosen so that the total number of one bits transmitted is odd.
Write a program that computes the parity bit for groups of 8 bits
entered by the user using even parity.
Your program should read strings containing 8 bits until the user enters a blank line.
After each string is entered by the user
your program should display a clear message indicating
whether the parity bit should be 0 or 1.
Display an appropriate error message if the user enters something other than 8 bits.

Hint: You should read the input from the user as a string.
Then you can use the count method
to help you determine the number of zeros and ones in the string.
Information about the count method is available online.
"""

# START Definition of FUNCTION


def valutaEntry(numero):
    if len(numero) == 8:
        for char in numero:
            if (char != "0") and (char != "1"):
                return False
        return True
    return False


def computesEvenParityBit(dataBit):
    if dataBit.count("1") % 2 == 0:     # number 1 -> even
        parityBit = "0"
    else:
        parityBit = "1"
    return parityBit


# END Definition of FUNCTION


# Declaration of VARIABLES
dataBit = "init"
dataBitValidated = True

# Acquisition and Control of the DATA entered by the USER
while dataBit != "":
    if dataBitValidated:
        dataBit = input("Enter the DATA (8bit) to be TRANSMITTED (or EMPTY line to QUIT): ")
        dataBitValidated = valutaEntry(dataBit)
        # EVEN PARITY BIT computing
        parityBit = computesEvenParityBit(dataBit)
        if dataBit != "" and dataBitValidated:
            # Displaying the EVEN PARITY BIT
            print("The PARITY BIT to be appended at the data bits for the EVEN PARITY is " + \
                str(parityBit))
    else:
        print("Incorrect entry. Try again.")
        dataBit = input("Enter the DATA (8bit) to be TRANSMITTED (or EMPTY line to QUIT): ")
        dataBitValidated = valutaEntry(dataBit)
        # EVEN PARITY BIT computing
        parityBit = computesEvenParityBit(dataBit)
        if dataBit != "" and dataBitValidated:
            # Displaying the EVEN PARITY BIT
            print("The PARITY BIT to be appended at the data bits for the EVEN PARITY is " +
                  str(parityBit))
