"""
The program READS a FILE (whose NAME is provided by the USER) 
containing a LIST of WORDS
and randomly concatenates TWO WORDS to generate a PASSWORD (8-10 characters).
"""

# Import STRING and RANDOM modules
import string
import random


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
filename = input("Enter a FILE name for PASSWORD generation: ")

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
        filename = input("Enter a FILE name for PASSWORD generation: ")
    # Exception -> empty line
    except:
        print("Warning, NO FILE entered.")
        filename = input("Enter a FILE name for PASSWORD generation: ")


# LIST which will contain the WORDS
words = []

# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        # Length Word between 3 and 7 characters
        if 3 <= len(word) <= 7:
            words.append(word[0].upper()+word[1:].lower())

# PASSWORD generation
while True:
    password = random.choice(words) + random.choice(words)
    # Length password between 8 and 10 characters
    if 8 <= len(password) <= 10:
        break

# Closing the previously opened file
f_name_opened.close()

# Display of the generated password
print("GENERATED PASSWORD -> {}".format(password))
