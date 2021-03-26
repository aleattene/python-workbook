"""
The program receives from the USER a STRING
and returns (ignoring spaces and punctuation marks),
whether or not it is a PALINDROME.
"""


# START Definition of FUNCTION


def checkWord(string):
    string = string.upper()
    index_sx = 0                    # left index
    index_dx = len(string)-1        # right index
    check = 0

    while index_sx < index_dx:
        # CHECK characters
        if ("A" <= string[index_sx] <= "Z" or "0" <= string[index_sx] <= "9") and \
                ("A" <= string[index_dx] <= "Z" or "0" <= string[index_dx] <= "9"):
            check += 1
            if string[index_sx] != string[index_dx]:
                return "IS NOT a PALINDROME."
            index_sx += 1               # increasing left index
            index_dx -= 1               # decreasing right index
        elif ("A" <= string[index_sx] <= "Z" or "0" <= string[index_sx] <= "9") and \
                not("A" <= string[index_dx] <= "Z" or "0" <= string[index_dx] <= "9"):
            index_dx -= 1               # decreasing only right index
        elif not ("A" <= string[index_sx] <= "Z" or "0" <= string[index_sx] <= "9") and \
                ("A" <= string[index_dx] <= "Z" or "0" <= string[index_dx] <= "9"):
            index_sx += 1               # increasing left index
        else:
            index_sx += 1               # increasing left index
            index_dx -= 1               # decreasing right index

    if check > 0:
        return "IS a PALINDROME."
    else:
        return"IS NOT a CHARACTER STRING."


# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
word = input("Enter the STRING: ")


# Evaluation if STRING is a PALINDROME
palindrome = checkWord(word)


# Displaying the RESULT
print("\"" + word.upper() + "\" (ignoring spaces and punctuation marks) " + palindrome)
