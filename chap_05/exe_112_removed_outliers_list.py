"""
When analysing data collected as part of a science experiment
it may be desirable to remove the most extreme values before performing other calculations.
Write a function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the n smallest elements removed.
Then it should return the new copy of the list as the function’s only result.
The order of the elements in the returned list does not have to match the order of the elements in the original list.
Write a main program that demonstrates your function.
It should read a list of numbers from the user and
remove the two largest and two smallest values from it
by calling the function described previously.
Display the list with the outliers removed, followed by the original list.
Your program should generate an appropriate error message if the user enters less than 4 values.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):            # Possible evolution -> IMPORT module
    entry_list = values_string.split()    # ["value","value"]
    if len(entry_list) < 4:
        return False
    for value in entry_list:
        if not(value.isdigit()):
            return False
    return True


def removeOutliersList(original_values_list, n):
    values_list = original_values_list[:]          # copy original_values_list
    for i in range(len(values_list)):
        values_list[i] = int(values_list[i])       # conversion [str] -> [int]
    values_list.sort()
    return values_list[n:-n]                       # removed outliers


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    values_string = input(
        "Enter the VALUES (at least four) separated by a white space: ")
    values_string_checked = checkEntry(values_string)

    while not(values_string_checked):
        print("Incorrect entry. Try again.")
        values_string = input(
            "Enter the VALUES (at least four) separated by a white space: ")
        values_string_checked = checkEntry(values_string)

    # ORIGINAL LIST generation -> ["value","value"]
    original_values_list = values_string.split()
    for i in range(len(original_values_list)):
        # conversion [str] -> [int]
        original_values_list[i] = int(original_values_list[i])

    # NEW LIST with REMOVED OUTLIERS (2 smallest and 2 largest)
    outliers_removed = removeOutliersList(original_values_list, 2)

    # Displaying the RESULTS
    print("NEW LIST -> {}".format(outliers_removed))
    print("ORIGINAL LIST -> {}".format(original_values_list))


if __name__ == "__main__":
    main()
