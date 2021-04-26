"""
The program detects REPEATED WORDS in a TEXT FILE (whose NAME is provided as a COMMAND-LINE ARGUMENT)
and returns a message containing any REPEATED WORDS with the LINE NUMBER.
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


try:
    if len(sys.argv) != 2:
        raise Exception

    # Opening the file (sysargv[1]) in reading mode
    f_name_opened = open(sys.argv[1], "r")

# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[1]))
    quit()

# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()


# Dictionary which will contain the repeated words
repeated_words = {}

# Declaration of supporting data structures
all_words = []
map_line_index = {}
index = 0

# Select of the each Line from LIST of the LINES (returned from the readlines)
for num_line, line in enumerate(f_name_opened.readlines(), 1):
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        all_words.append(word)
        # mapping -> line number : [index]
        if num_line in map_line_index:
            map_line_index[num_line].append(index)
        else:
            map_line_index[num_line] = [index]
        index += 1


for i in range(len(all_words)-1):
    # Repeated Word
    if all_words[i] == all_words[i+1]:
        # reverse mapping -> [index] : line number
        for k in map_line_index:
            if (i+1) in map_line_index[k]:
                number_line = k
        # Population of the dictionary containing the repeated words -> word : [line number]
        if all_words[i+1] in repeated_words:
            repeated_words[all_words[i+1]].append(number_line)
        else:
            repeated_words[all_words[i+1]] = [number_line]


# Closing the previously opened files
f_name_opened.close()


# Displaying the RESULTS
if len(repeated_words) == 0:
    print("NO REPEATED WORDS")
else:
    print("REPEATED WORD: ")
    for word in repeated_words:
        print("\"{}\" -> ".format(word), end="")
        for value in repeated_words[word]:
            print("line {} ".format(value), end=" ")
        print()
