"""
In this exercise you will create a program that identifies all of the words in a string entered by the user.
Begin by writing a function that takes a string as its only parameter.
Your function should return a list of the words in the string with the punctuation marks at the edges of the words removed. The punctu- ation marks that you must consider include commas, periods, question marks, hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove punctuation marks that appear in the middle of a word, such as the apostrophes used to form a contraction. For example, if your function is provided with the string "Contractions include: don’t, isn’t, and wouldn’t." then your function should return the list ["Contractions", "include", "don’t", "isn’t", "and", "wouldn’t"]. Write a main program that demonstrates your function. It should read a string from the user and then display all of the words in the string with the punctuation marks removed.
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
