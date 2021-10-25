"""
The program receives from the USER a STRING
and returns (displaying it) whether or not it is a PALINDROME.
"""


# START Definition of FUNCTION

def checkWord(string):
    string = string.upper()
    index_sx = 0                    # left index
    index_dx = len(string)-1        # right index
    while index_sx < index_dx:
        if string[index_sx] != string[index_dx]:
            return "IS NOT a PALINDROME."
        index_sx += 1               # increasing left index
        index_dx -= 1               # decreasing right index
    return "IS a PALINDROME."


# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
word = input("Enter the STRING: ")


# Evaluation if STRING is a PALINDROME
palindrome = checkWord(word)


# Displaying the RESULT
print("\"" + word.upper() + "\" " + palindrome)