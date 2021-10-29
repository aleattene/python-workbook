"""
The program receives a NUMBER from the USER
and returns (displaying it) its SQUARE ROOT,
computed with the NEWTON'S METHOD.
"""


# START Definition of FUNCTIONS


def checkEntry(number):
    # possible evolution -> check POSITIVE (int or float)
    return True


def squareRoot(number, guess=1.0):
    # NEWTON'S method
    if abs(number - (guess ** 2)) < (10 ** (-12) * number):
        return guess
    else:
        return squareRoot(number, ((guess + (number / guess)) / 2))


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    while True:
        number = input("Enter a positive NUMBER: ")
        if checkEntry(number):
            break

    # STRING TESTING (expected value = 95726656)
    # number = "9163592668942336"

    # SQUARE ROOT computing
    guess = squareRoot(float(number))

    # Displaying the SQUARE ROOT computed
    print("The SQUARE ROOT of ({}) is approximately {:.2f}".format(number, guess))


if __name__ == "__main__":
    main()
