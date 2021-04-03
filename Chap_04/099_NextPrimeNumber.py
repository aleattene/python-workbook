"""
The program receives from the USER an INTEGER NUMBER
and returns (displaying it) the FIRST PRIME NUMBER
LARGER than the ENTERED INTEGER NUMBER.
"""


# START Definition of the FUNCTIONS


def valutaEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INT POSITIVE
    return True


def primeNumber(number):            # Possible evolution -> IMPORT module
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


def nextPrime(number):
    next_prime = int(number) + 1
    while not(primeNumber(next_prime)):
        next_prime += 1
    return next_prime


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter an INTEGER NUMBER: ")

    # Computing of the FIRST PRIME number larger than "NUMBER".
    next_prime_number = nextPrime(number)

    # Displaying the RESULTS
    print("The FIRST PRIME number LARGER than {:02d} is \"{:02d}\"".format(
        int(number), next_prime_number))


if __name__ == "__main__":
    main()
