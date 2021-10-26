"""
The program receives a STRING from the USER
and return (displaying it) the same STRING FORMATTED in the following manner:
- capitalized the FIRST non-space CHARACTER
- capitalized the first non-space character AFTER a period,
    exclamation mark or question mark
- capitalized a lowercase "i" if it is preceded by a space,period, 
    exclamation mark, question mark or followed by an apostrophe.
"""


# START Definition of FUNCTIONS


def capitalizeString(string):           # Possible evolution -> FUNCTION REFACTORING
    length = len(string)
    if length < 1:
        return ""
    new_string = []
    i = 0
    while string[i] == " ":
        new_string.append(string[i])
        i += 1
    new_string.append(string[i].upper())
    i += 1
    while i < length-1:
        if string[i] == "i" and \
            (string[i-1] == " " or string[i-1] == "." or string[i-1] == "!" or
             string[i-1] == "?" or string[i+1] == "'"):
            new_string.append(string[i].upper())
        elif string[i] == "." or string[i] == "!" or string[i] == "?":
            new_string.append(string[i])
            if i == length-2:
                break
            while string[i+1] == " ":
                new_string.append(string[i+1])
                i += 1
                if i == length-2:
                    break
            new_string.append(string[i+1].upper())
            i += 1
        else:
            new_string.append(string[i])
        i += 1
    if i == (length-1):
        if string[i] == "i" and \
            (string[i-1] == " " or string[i-1] == "." or string[i-1] == "!" or
                string[i-1] == "?"):
            new_string.append(string[i].upper())
        else:
            new_string.append(string[i])
    return "".join(new_string)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    string = input("Enter the STRING to CAPITALIZE: ")

    # STRING testing
    # string = "   what time do i have to be there? what's the address?" + \
    #     " this time i'll try to be on time!"

    # Displaying the RESULTS
    print("   ORIGINAL STRING -> " + string)
    print("CAPITALIZED STRING -> " + capitalizeString(string))


if __name__ == "__main__":
    main()
