"""
The program determines and displays the WORD (or WORDS) 
that occur MOST FREQUENTLY in a FILE 
whose NAME is provided by the USER.
"""

# Import STRING module
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


# Acquisition of the file name by the user
filename = input("Enter the FILE name to be analyzed: ")

open_file = True
while open_file:
    try:
        if filename == "":
            raise Exception
        # Opening the file name in read mode
        f_name_opened = open(filename, "r")
        open_file = False
    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(filename))
        filename = input("Enter the FILE name to be analyzed: ")
    # Exception -> empty line
    except:
        print("Warning, NO FILE entered.")
        filename = input("Enter the FILE name to be analyzed: ")


# Declaration of the dictionary which will contain the frequency of the words
words_frequency = {}

# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        # Word already present in the dictionary -> frequency counter increment
        if word.lower() in words_frequency:
            words_frequency[word.lower()] += 1
        else:
            # Word not present in the dictionary -> added new element
            words_frequency[word.lower()] = 1

# Closing the previously opened file
f_name_opened.close()

# Displaying the RESULTS
print("*** WORD(s) that appears MOST FREQUENTLY in the file \"{}\"  ***".format(filename))
max_frequency = max(words_frequency.values())
for k in words_frequency:
    if words_frequency[k] == max_frequency:
        print(k + " : " + str(words_frequency[k]))
