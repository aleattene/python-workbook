"""
The program receives INTEGERS from the USER and stores them in a LIST. 
The insertion continues until the user inserts ZERO.
After that, the program displays ALL of the VALUES entered by the user 
(except for the zero) in ASCENDING ORDER (with one value on each line).
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
