"""
The program receives several STRINGS from the USER
UNTIL a BLANK LINE is ENTERED.
After that, the program displays all of the STRINGS entered, 
formatted in the FOLLOWING MANNER:
- 1 item entered -> item
- 2 items entered -> item and item
- 3 items entered -> item, item and item
- 4 items entered -> item, item, item and item
- n items entered -> item, item, [...], item and item
"""


# START Definition of the FUNCTION


def checkEntry(number):
    # Check Entry -> STR
    return True


def formatStringList(string_list):
    length_list = len(string_list)
    all_string = ""
    if length_list == 0:
        all_string += "NO ITEMS ENTERED."
    if length_list == 1:
        all_string += string_list[0]
    elif length_list == 2:
        all_string += string_list[0] + " and " + string_list[1]
    elif length_list > 2:
        for i in range(length_list-2):
            all_string += string_list[i] + ", "
        all_string += string_list[-2] + " and " + string_list[-1]
    return all_string


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # EMPTY LIST
    string_list = []

    # Acquisition and Control of the DATA entered by the USER
    string = input("Enter the STRING (blank line to quit): ")

    while string != "":
        string_list.append(string)
        string = input("Enter the STRING (blank line to quit): ")

    # Displaying the RESULTS
    print(formatStringList(string_list))


if __name__ == "__main__":
    main()
