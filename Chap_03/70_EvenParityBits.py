"""
The program receives from the USER the DATA (8 bits) to be transmitted
and returns (displaying it) the BIT of EVEN PARITY to be appended at the eight data bits.
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
            print("The PARITY BIT to be appended at the data bits for the EVEN PARITY is " + \
                str(parityBit))
