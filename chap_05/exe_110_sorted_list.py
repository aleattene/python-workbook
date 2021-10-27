"""
Write a program that reads integers from the user and stores them in an array.
Your program should continue reading values until the user enters 0.
Then it should display all of the values entered by the user (except for the 0) in ascending order,
with one value appearing on each line.
Use either the sort method or the sorted function to sort the array.
"""


# START Definition of the FUNCTIONS


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER
    return True


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # EMPTY list
    integers = []

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the INTEGER NUMBER (zero to quit): ")

    while number != "0":
        integers.append(int(number))
        number = input("Enter the INTEGER NUMBER (zero to quit): ")

    # LIST ORDERING
    integers.sort()

    # Displaying the RESULTS
    for element in integers:
        print(element)


if __name__ == "__main__":
    main()
