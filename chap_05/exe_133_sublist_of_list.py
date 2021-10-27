"""
The program receives TWO LISTS OF INTEGERS from the USER
and returns whether or not the SECOND LIST is a SUBLIST of the FIRST,
also considering that:
- an EMPTY list IS a SUBLIST of ANY other list 
    (for example [] is a sublist of [1,2,3,4])
- ANY LIST IS a SUBLIST of ITSELF 
    (for example [1,2,3,4] is a sublist of [1,2,3,4])
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY LISTS
    pass


def isSublist(original_values_list, original_values_sublist):
    # EMPTY LIST (second list)
    if original_values_sublist == []:
        return True
    # CHECK ITEMS first list
    for i_list in range(len(original_values_list)):
        i_sublist = 0
        # ITEM of the FIRST LIST matches the FIRST ELEMENT of the SECOND list
        while original_values_list[i_list] == original_values_sublist[i_sublist]:
            # ALL the ITEMS of the SUBLIST match the ELEMENTS of the FIRST list
            if i_sublist == len(original_values_sublist)-1:
                return True
            # NOT ALL the ITEMS of the SUBLIST match the ELEMENTS of the FIRST list
            elif i_list == len(original_values_list)-1:
                return False
            # ITEM of the FIRST LIST matches ELEMENT of the SECOND list
            else:
                i_list += 1
                i_sublist += 1
                continue
    return False


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # # Acquisition of DATA entered by the USER
    list_number = input(
        "Enter the NUMBERS separated by a white space for the FIRST LIST: ")
    sublist_number = input(
        "Enter the NUMBERS separated by a white space for the FIRST LIST: ")

    # STRING TESTING
    # list_number = "1 2 3 4"
    # sublist_number = "1 2 3 4"

    # LISTS generation -> ["value","value"]
    original_values_list = list_number.split()
    original_values_sublist = sublist_number.split()

    # LISTS conversion [STR] -> [INT]
    for i in range(len(original_values_list)):
        original_values_list[i] = int(original_values_list[i])
    for i in range(len(original_values_sublist)):
        original_values_sublist[i] = int(original_values_sublist[i])

    # SUBLIST evaluation
    sublist = isSublist(original_values_list, original_values_sublist)
    if sublist:
        result = "IS a"
    else:
        result = "IS NOT a"

    # Displaying the RESULT
    print("The LIST {} {} SUBLIST of the LIST {}".format(
        original_values_sublist, result, original_values_list))


if __name__ == "__main__":
    main()
