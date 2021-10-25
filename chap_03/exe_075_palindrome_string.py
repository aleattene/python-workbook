"""
A string is a palindrome if it is identical forward and backward.
For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.

Write a program that reads a string from the user and
uses a loop to determine whether or not it is a palindrome.
Display the result, including a meaningful output message.

Aibohphobia is the extreme or irrational fear of palindromes.

This word was constructed by prepending the -phobia suffix with it’s reverse,
resulting in a palindrome.

Ailihphilia is the fondness for or love of palindromes.

It was constructed in the same manner from the -philia suffix.
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