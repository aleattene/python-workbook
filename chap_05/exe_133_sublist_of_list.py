"""
A sublist is a list that is part of a larger list.
A sublist may be a list containing a single element, multiple elements, or even no elements at all.

For example:
[1], [2], [3] and [4] are all sublists of [1, 2, 3, 4].

The list [2, 3] is also a sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4]
because the elements 2 and 4 are not adjacent in the longer list.

The empty list is a sublist of any list.
As a result, [] is a sublist of [1, 2, 3, 4].

A list is a sublist of itself, meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].

In this exercise you will create a function, isSublist,
that determines whether or not one list is a sublist of another.
Your function should take two lists, larger and smaller, as its only parameters.
It should return True if and only if smaller is a sublist of larger.
Write a main program that demonstrates your function.
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
