"""
Write a function that takes a string, s, as its first parameter, and
the width of the window in characters, w, as its second parameter.
Your function will return a new string that includes
whatever leading spaces are needed
so that s will be centered in the window when the new string is printed.

The new string should be constructed in the following manner:
- if the length of s is greater than or equal to the width of the window then s should be returned
- if the length of s is less than the width of the window
    then a string containing (len(s) - w) // 2 spaces followed by s should be returned.

Write a main program that demonstrates your function by displaying multiple strings centered in the window.
"""


# START Definition of FUNCTIONS


def valutaEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INT POSITIVE
    return True


def centerString(s, w):
    w = int(w)
    if len(s) >= w:
        return s
    else:
        spaces = (w - len(s)) // 2
        return (" " * spaces) + s + (" " * spaces)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    print("Enter the STRING and the WIDTH of the WINDOWS.")
    string = input("STRING: ")
    width_window = input("WIDTH (number of characters): ")
    width_window_validated = valutaEntry(width_window)

    while not(width_window_validated):
        print("Incorrect entry. Try again.")
        print("Enter the STRING and the WIDTH of the WINDOWS.")
        string = input("STRING: ")
        width_window = input("WIDTH (number of characters): ")
        width_window_validated = valutaEntry(width_window)

    # Displaying the RESULTS
    result = centerString(string, width_window)
    print("|" + result + "|")


if __name__ == "__main__":
    main()
