"""
The program receives a LIST OF NUMBERS from the USER
and returns whether or not it is a SORTED LIST.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):            # Possible evolution -> IMPORT module
    entry_list = values_string.split()    # ["value","value"]
    for value in entry_list:
        if not(value.isdigit()):          # possible evolution -> int and float
            return False
    return True


def evaluationSortedOrder(original_values_list):
    length_list = len(original_values_list)
    if length_list <= 2:
        return True
    index = 0
    while index < (length_list-1):
        if float(original_values_list[index]) == float(original_values_list[index+1]):
            index += 1
        else:
            break
    if index == (length_list-1):
        return True
    elif float(original_values_list[index]) < float(original_values_list[index+1]):
        for i in range(index+1, length_list-1):
            if float(original_values_list[i]) > float(original_values_list[i+1]):
                return False
    elif float(original_values_list[index]) > float(original_values_list[index+1]):
        for i in range(index+1, length_list-1):
            if float(original_values_list[i]) < float(original_values_list[i+1]):
                return False
    return True


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    numbers = input("Enter the NUMBERS separated by a white space: ")
    numbers_checked = checkEntry(numbers)

    while not(numbers_checked):
        print("Incorrect entry. Try again.")
        numbers = input("Enter the NUMBERS separated by a white space: ")
        numbers_checked = checkEntry(numbers)

    # LIST generation -> ["value","value"]
    original_values_list = numbers.split()

    # Evaluation of the ORDERING of the LIST (True or False)
    sorted_list = evaluationSortedOrder(original_values_list)

    # Displaying the RESULTS
    print("The LIST of NUMBERS entered is ", end="")
    if sorted_list:  # true
        print("a SORTED LIST.")
    else:  # false
        print("NOT a SORTED LIST.")


if __name__ == "__main__":
    main()
