"""
The program receives A LIST OF INTEGERS from the USER
and returns ALL SUBLIST of THIS LIST,
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


def allSublists(original_values_list):
    # EMPTY LIST (sublist of any list)
    sublists = [[]]
    lenght_list = len(original_values_list)
    if lenght_list > 0:
        for index_value in range(len(original_values_list)):
            sx = 0
            dx = index_value + 1
            for i in range(len(original_values_list)):
                sublist = original_values_list[sx:dx]
                sublists.append(sublist)
                if dx < lenght_list:
                    sx += 1
                    dx += 1
                else:
                    break
    return sublists


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # # Acquisition of DATA entered by the USER
    list_number = input(
        "Enter the NUMBERS separated by a white space for inserting the LIST: ")

    # STRING TESTING
    # list_number = "1 2 3"

    # LIST generation -> ["value","value"]
    original_values_list = list_number.split()

    # LIST conversion [STR] -> [INT]
    for i in range(len(original_values_list)):
        original_values_list[i] = int(original_values_list[i])

    # SUBLISTS generation
    sublists = allSublists(original_values_list)
    if len(sublists) > 1:
        sub_subs = "SUBLISTS"
        article = "are"
    else:
        sub_subs = "SUBLIST"
        article = "is"

    # Displaying the RESULTS
    print("The {} of the LIST {} {}:".format(
        sub_subs, original_values_list, article))
    for item in sublists:
        print(item, end=" ")


if __name__ == "__main__":
    main()
