"""
A string is a palindrome if it is identical forward and backward.
For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.

Such palindromes examined the characters in a string,
possibly ignoring spacing and punctuation marks,
to see if the string was the same forwards and backwards.
While palindromes are most commonly considered character by character,
the notion of a palindrome can be extended to larger units.

For example, while the sentence

“Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?”

isn’t a character by character palindrome,
it is a palindrome when examined a word at a time (and when capitalization and punctuation are ignored).

Other examples of word by word palindromes include

“Herb the sage eats sage, the herb” and “Information school graduate seeks graduate school information”.

Create a program that reads a string from the user.
Your program should report whether or not the entered string is a word by word palindrome.
Ignore spacing and punctuation when determining the result.
"""


# START Definition of the FUNCTION


# Possible evolution -> check string entered by the user
def checkEntry(string):
    pass


def removePunctuationMarks(original_string):
    punctuation_marks = [",", ".", "?", "!", "-", "_", "'", ":", ";", "\"", ]
    words_list = original_string.lower().split()
    for i in range(len(words_list)):
        # Initial position of the word
        while (words_list[i][0]) in punctuation_marks:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][0], "")
        # Final position of the word
        while (words_list[i][-1]) in punctuation_marks:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][-1], "")
    return words_list


def checkWordByWord(original_string):
    words_list = removePunctuationMarks(original_string)
    index_sx = 0                        # left index
    index_dx = len(words_list)-1        # right index
    while index_sx < index_dx:
        if words_list[index_sx] != words_list[index_dx]:
            return "IS NOT a PALINDROME."
        index_sx += 1                   # increasing left index
        index_dx -= 1                   # decreasing right index
    return "IS a PALINDROME."


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    original_string = input("Enter the STRING: ")
    # TEST STRINGS
    # original_string = "Is it crazy how saying sentences backward sentences saying how crazy it is"
    # original_string = "Herb the sage eats sage, the herb"
    # original_string = "Information school graduate seeks graduate school information"

    # Evaluation if STRING is a PALINDROME
    palindrome = checkWordByWord(original_string)

    # Displaying the RESULT
    print("The STRING \"{}\" {}".format(original_string, palindrome))


if __name__ == "__main__":
    main()
