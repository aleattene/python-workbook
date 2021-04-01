"""
The program receives from the USER an INTEGER NUMBER
and returns (displaying it) whether or not it is PRIME.
"""


# START Definition of the FUNCTIONS


def valutaEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INT POSITIVE
    return True


def primeNumber(number):
    number = int(number)
    # NUMBER = 1
    if number == 1:
        return True
    # NUMBER > 1
    if number > 1:
        for i in range(2, number):
            if (number % i == 0):   # divisible number
                return False
        return True


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter an INTEGER NUMBER: ")

    # PRIME NUMBER evaluation
    prime_number = primeNumber(number)

    # Displaying the RESULTS
    print("The NUMBER {:02d}".format(int(number)), end="")
    if prime_number:
        print(" IS a PRIME NUMBER.")
    else:
        print(" IS NOT a PRIME NUMBER.")


if __name__ == "__main__":
    main()
