"""
Write a program that reads integers from the user and stores them in an array.
Use 0 as a sentinel value to mark the end of the input.
Once all of the values have been read your program should display them (except for the 0) in reverse order,
with one value appearing on each line.
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
