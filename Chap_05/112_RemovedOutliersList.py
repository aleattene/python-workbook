"""
The program receives a LIST of NUMBERS (at least four) from the USER 
and REMOVES the TWO LARGEST and TWO SMALLEST VALUES within the LIST. 
After that, displays the NEW LIST with the OUTLIERS REMOVED,
following by the ORIGINAL LIST of VALUES.
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
