"""
The program displays the PRIME NUMBERS
between 2 and a LIMIT NUMBER entered by the USER,
using the SIEVE of ERATOSTHENES.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY -> INT
    pass


def primeNumbers(limit_number):
    limit_number = int(limit_number)
    # EMPTY list
    numbers_list = []
    # VALUES from 0 to limit_number included
    for i in range(limit_number+1):
        numbers_list.append(i)
    # Cross out 0 and 1 because they are NOT PRIME
    if len(numbers_list) > 1:
        numbers_list[0] = 0
        numbers_list[1] = 0
    # Set p equal to 2
    p = 2
    while p < limit_number:
        # Cross out multiples of p (but not p itself)
        for i in range(p * 2, limit_number+1, p):
            numbers_list[i] = 0
        p += 1
        # Set p equal the next number in the list that is not crossed out
        while numbers_list[p] == 0:
            p += 1
            if p == len(numbers_list):
                break
    # OVER 100000 -> WARNING for computational overload
    """
    while i >= 0:
        if numbers_list[i] == 0:
            del numbers_list[i]
        i -= 1
    """
    return numbers_list


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # # Acquisition of DATA entered by the USER
    limit_number = input("Enter the LIMIT NUMBER: ")

    # STRING TESTING
    # limit_number = 1000000

    # Displaying the RESULTS
    print("PRIME NUMBERS (from 2 to {}):".format(limit_number))
    for number in primeNumbers(limit_number):
        if number != 0:
            print(number, end=" ")


if __name__ == "__main__":
    main()
