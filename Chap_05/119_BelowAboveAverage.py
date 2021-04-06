"""
The program receives INTEGERS from the USER UNTIL a BLANK LINE is ENTERED.
After that, the program displays:
- ALL of the ENTERED VALUES
- The AVERAGE VALUE
- ALL of the BELOW AVERAGE VALUES
- ALL of the AVERAGE VALUES
- ALL of the ABOVE AVERAGE VALUES
"""


# START Definition of the FUNCTION


def checkEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INTEGER
    return True


def computeAverageValues(numbers):
    average_value = sum(numbers) / len(numbers)
    return average_value


def computeBelowAboveAverage(numbers, average_value):
    below_values = []
    average_values = []
    above_values = []
    all_values = []
    for number in numbers:
        if number < average_value:
            below_values.append(number)
        elif number == average_value:
            average_values.append(number)
        else:
            above_values.append(number)
    below_values.sort()
    above_values.sort()
    all_values.append(below_values)
    all_values.append(average_values)
    all_values.append(above_values)
    return all_values

# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # EMPTY LIST
    numbers = []

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter the NUMBER (blank line to quit): ")

    while number != "":
        numbers.append(int(number))
        number = input("Enter the NUMBER (blank line to quit): ")

    # AVERAGE VALUE computing
    average_value = computeAverageValues(numbers)

    # LIST of the LIST -> [[below average values],[average values],[above average values]]
    all_values = computeBelowAboveAverage(numbers, average_value)

    # Displaying the RESULTS
    print("VALUES ENTERED: ", end="")
    for number in numbers:
        print(str(number) + " ", end="")

    print("\nAVERAGE VALUE = {}".format(average_value))

    print("BELOW average values -> ", end="")
    if len(all_values[0]) == 0:
        print("NO VALUE", end="")
    else:
        for number in all_values[0]:
            print(str(number) + " ", end="")

    print("\nAVERAGE values -> ", end="")
    if len(all_values[1]) == 0:
        print("NO VALUE", end="")
    else:
        for number in all_values[1]:
            print(str(number) + " ", end="")

    print("\nABOVE average values -> ", end="")
    if len(all_values[2]) == 0:
        print("NO VALUE", end="")
    else:
        for number in all_values[2]:
            print(str(number) + " ", end="")


if __name__ == "__main__":
    main()
