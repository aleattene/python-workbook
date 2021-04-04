"""
The program receives INTEGERS from the USER and STORES them in a LIST. 
The insertion CONTINUES UNTIL the user inserts ZERO.
After that, the program displays ALL of the VALUES entered by the user 
(except for the zero) in REVERSE ORDER (with one value on each line).
"""


# START Definition of the FUNCTION


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER
    return True


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # EMPTY list
    integers = []

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the INTEGER NUMBER (zero to quit): ")

    while number != "0":
        integers.append(int(number))
        number = input("Enter the INTEGER NUMBER (zero to quit): ")

    # REVERSAL of the LIST ORDER
    integers.reverse()

    # Displaying the RESULTS
    for element in integers:
        print(element)


if __name__ == "__main__":
    main()
