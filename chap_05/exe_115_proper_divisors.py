"""
The program receives a POSITIVE INTEGER from the USER
and returns (displaying it) its PROPER DIVISORS.
For example, 6 has only 1, 2, and 3 as PROPER DIVISORS,
as 6 is an IMPROPER DIVISOR.
"""


# START Definition of the FUNCTIONS


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER POSITIVE
    return True


def computeProperDivisors(number):  # Possible evolution -> REFACTORING
    number = int(number)
    divisors = [1]
    divisor = 2
    quotient = number
    while divisor < quotient:
        if number % divisor == 0:
            divisors.append(divisor)
            quotient = number // divisor
            if quotient > divisor:
                divisors.append(quotient)
            divisor += 1
        else:
            divisor += 1
    divisors.sort()
    for i in range(len(divisors)):
        divisors[i] = str(divisors[i])      # Conversion [INT] -> [STR]
    return divisors


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the POSITIVE INTEGER: ")

    # LIST of the PROPER DIVISORS to the NUMBER -> ["proper divisor","proper divisor" ]
    proper_divisors_list = computeProperDivisors(number)
    # "proper divisor, proper divisor"
    proper_divisors = ",".join(proper_divisors_list)

    # Displaying the RESULTS
    if len(proper_divisors) == 1:
        print("The PROPER DIVISOR of the NUMBER ({}) is ({}), ".format(
            number, proper_divisors), end="")
        print("therefore ({}) is a PRIME NUMBER.".format(number))
    else:   # len(proper_divisors) > 1
        print("The PROPER DIVISORS of the NUMBER ({}) are ({}).".format(
            number, proper_divisors))


if __name__ == "__main__":
    main()
