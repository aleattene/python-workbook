"""
The program receives a STRING from the USER
and after REMOVING the PUNCTUATION MARKS 
(except those that appear in the middle of the words), 
it RETURNS (displaying it) the LIST of the WORDS making up the string itself.
Punctuation Marks to remove: commas, periods, question marks,
hyphens, apostrophes, exclamation points, colons, and semicolons.
"""


# START Definition of the FUNCTION

# Possible evolution -> check string entered by the user
def checkEntry(string):
    pass


def removePunctuationMarks(original_string):
    punctuation_marks = [",", ".", "?", "!", "-", "_", "'", ":", ";", "\"", ]
    words_list = original_string.split()
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


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    original_string = input("Enter the STRING: ")
    # TEST STRING
    #original_string = "Contractions include: don't, isn't, and wouldn't."

    # Displaying the RESULTS
    print("ORIGINAL STRING -> {}".format(original_string))
    print("WORDS LIST -> ", end="")
    print(removePunctuationMarks(original_string))


if __name__ == "__main__":
    main()
