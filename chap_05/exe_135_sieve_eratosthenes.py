"""
The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago
to easily find all of the prime numbers between 2 and some limit, say 100.

A description of the algorithm follows:
Write down all of the numbers from 0 to the limit
    Cross out 0 and 1 because they are not prime
    Set p equal to 2
While p is less than the limit do
    Cross out all multiples of p (but not p itself)
    Set p equal to the next number in the list that is not crossed out
Report all of the numbers that have not been crossed out as prime

The key to this algorithm is that it is relatively easy to cross out every nth number on a piece of paper.
This is also an easy task for a computer a for loop can simulate this behavior
when a third parameter is provided to the range function.

When a number is crossed out, we know that it is no longer prime,
but it still occupies space on the piece of paper,
and must still be considered when computing later prime numbers.
As a result, you should not simulate crossing out a number by removing it from the list.
Instead, you should simulate crossing out a number by replacing it with 0.
Then, once the algorithm completes, all of the non-zero values in the list are prime.

Create a program that uses this algorithm
to display all of the prime numbers between 2 and a limit entered by the user.
If you implement the algorithm correctly
you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.
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
