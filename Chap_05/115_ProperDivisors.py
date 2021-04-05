"""
The program receives a POSITIVE INTEGER from the USER
and returns (displaying it) its PROPER DIVISORS.
For example, 6 has only 2 and 3 as PROPER DIVISORS, 
    because 1 and 6 are IMPROPER DIVISORS.
"""


# START Definition of the FUNCTIONS


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER POSITIVE
    return True


def computeProperDivisors(number):  # Possible evolution -> REFACTORING
    number = int(number)
    divisors = []
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
    if len(proper_divisors) == 0:
        print("The NUMBER ({}) has NOT a PROPER DIVISORS as it is a PRIME NUMBER.".format(number))
    elif len(proper_divisors) == 1:
        sign = ""
        verb = "is"
        print("The PROPER DIVISOR{} of the NUMBER ({}) {} ({}).".format(
            sign, number, verb, proper_divisors))
    else:   # len(proper_divisors) > 1
        sign = "S"
        verb = "are"
        print("The PROPER DIVISOR{} of the NUMBER ({}) {} ({}).".format(
            sign, number, verb, proper_divisors))


if __name__ == "__main__":
    main()
