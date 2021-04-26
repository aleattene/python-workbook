"""
The program READS a FILE (whose NAME is provided by the USER as a COMMAND-LINE ARGUMENT)
and returns ALL of the WORDS in it that are MISSPELLED
(not presents in a list containing the know words).
"""


# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys
import string


# START Definition of the FUNCTION


# possible evolution -> import function
def removePunctuationMarks(original_string):
    words_list = original_string.split()
    for i in range(len(words_list)):
        # Initial position of the word
        while (words_list[i][0]) in string.punctuation:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][0], "")
        # Final position of the word
        while (words_list[i][-1]) in string.punctuation:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][-1], "")
    return words_list


# END Definition of the FUNCTION


# Constant declaration
WORDS_NOTE = "words.txt"


try:
    if len(sys.argv) != 2:
        raise Exception
    # Opening the files in reading mode
    f_name_words_notes = open(WORDS_NOTE, "r")
    f_name_opened = open(sys.argv[1], "r")
# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[1]))
    quit()
# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()


# Dictionary which will contain the know words
words_notes = {}
# List which will contain the spelling mistakes
mistakes = []


# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_words_notes.readlines():
    # Dictionary population
    words_notes[line.strip().lower()] = 0


# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        if word.lower() not in words_notes:
            # Word not present in the dictionary -> added new element at the list of the spelling mistakes
            mistakes.append(word)


# Closing the previously opened files
f_name_words_notes.close()
f_name_opened.close()


# Displaying the RESULTS
print("In the analysis of the file \"{}\" were found the following spelling errors:".format(
    sys.argv[1]))
for word in mistakes:
    print(word, end="  ")
