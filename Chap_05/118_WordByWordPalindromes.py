"""
The program receives from the USER a STRING composed of SEVERAL WORDS
and RETURNS whether or not it IS a PALINDROME
(ignoring spacing, capitalizing, and punctuation marks).
Punctuation Marks to ignore: commas, periods, question marks,
hyphens, apostrophes, exclamation points, colons, and semicolons.
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
