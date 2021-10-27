"""
When writing out a list of items in English, one normally separates the items with commas.
In addition, the word “and” is normally included before the last item, unless the list only contains one item.

Consider the following four lists:
- apples
- apples and oranges
- apples, oranges and bananas
- apples, oranges, bananas and lemons

Write a function that takes a list of strings as its only parameter.
Your function should return a string that contains all of the items in the list,
formatted in the manner described previously, as its only result.

While the examples shown previously only include lists containing four elements or less,
your function should behave correctly for lists of any length.

Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the function.

Summarizing:
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
