"""
The program receives a STRING and the WIDTH of the terminal WINDOW (in CHARACTERS) from the USER
and returns (displaying it) the STRING FORMATTED in the following manner:
- if the length of the string is greater than or equal to the width of the terminal window
    then only the string should be returned
- otherwise, the string must be returned with the addition of
    ((width - length(string)) // 2) spaces at precede and follow it
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
