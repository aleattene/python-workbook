"""
The program receives INTEGERS from the USER UNTIL a BLANK LINE is ENTERED.
After that, the program displays ALL of the NEGATIVE NUMBERS,
followed by ALL of the ZEROS, followed by ALL of the POSITIVE NUMBERS.
WITHIN EACH GROUP the NUMBERS is DISPLAYING in the SAME ORDER (each value on its own line)
that they WERE ENTERED by the USER.
For example: 3,-4,1,0,-1,0,-2,"" -> -4,-1,-2,0,0,3,1
"""


# START Definition of the FUNCTION


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER
    return True


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # EMPTY LISTS within an EMPTY LIST
    numbers = [[], [], []]     # [ [negatives] , [zeros] , [positives] ]

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the NUMBER (blank line to quit): ")

    while number != "":
        number = int(number)
        if number < 0:
            numbers[0].append(number)
        elif number == 0:
            numbers[1].append(number)
        else:   # number > 0
            numbers[2].append(number)
        number = input("Enter the NUMBER (blank line to quit): ")

    # Displaying the RESULTS
    for list_number in numbers:
        for number in list_number:
            print(number)


if __name__ == "__main__":
    main()
