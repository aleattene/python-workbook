"""
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n.

For example:
28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.

Write a function that determines whether or not a positive integer is perfect.
Your function will take one parameter:
- if that parameter is a perfect number then your function will return True,
- otherwise it will return False.

In addition, write a main program that uses your function
to identify and display all of the perfect numbers between 1 and 10,000.
"""


# START Definition of the FUNCTIONS


def computeProperDivisors(number):
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
    return divisors


def perfectNumber(number):
    # LIST of the PROPER DIVISORS to the NUMBER -> [proper divisor,proper divisor]
    proper_divisors_list = computeProperDivisors(number)
    sum_proper_divisors = sum(proper_divisors_list)
    if sum_proper_divisors == number:
        return True
    else:
        return False


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Displaying the RESULTS
    print("******************************************")
    print("| PERFECT NUMBERS (between 1 and 10.000) !")
    print("******************************************")
    item = 1
    for i in range(1, 10001):
        if perfectNumber(i):
            print("  " + str(item) + ") " + str(i) + " is a PERFECT NUMBER")
            item += 1
    print("******************************************")


if __name__ == "__main__":
    main()
