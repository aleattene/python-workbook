"""
Many people do not use capital letters correctly, especially when typing on small devices like smart phones.
To help address this situation,
you will create a function that takes a string as its only parameter and
returns a new copy of the string that has been correctly capitalized.

In particular, your function must:
- capitalize the first non-space character in the string,
- capitalize the first non-space character after a period, exclamation mark or question mark, and
- capitalize a lowercase “i” if it is preceded by a space and followed by
    a space, period, exclamation mark, question mark or apostrophe.

Implementing these transformations will correct most capitalization errors.

For example, if the function is provided with the string

“what time do i have to be there? what’s the address? this time i’ll try to be on time!” then it should

return the string

“What time do I have to be there? What’s the address? This time I’ll try to be on time!”.

Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.
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
