"""
The program READS a LIST of WORDS from a FILE
and determines what proportion of the words use each letter of the alphabet.
After that, it also displays the LETTER that is used in the SMALLEST PROPORTION of the words.
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


# FILE TO OPEN
FILE_TO_OPEN = "words.txt"

# Opening the file in reading mode
open_file = True
while open_file:
    try:
        f_name_opened = open(FILE_TO_OPEN, "r")
        open_file = False
    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(FILE_TO_OPEN))
        quit()


# Definition of the dictionary (letter -> number of the words that using the letter)
letter_to_words = {
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0,
    "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
    "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
}


# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        # Check if the letters in the dictionary are present in the word
        for k in letter_to_words:
            # The letter is present in the word
            if k in word.upper():
                # Increment of the counter
                letter_to_words[k] += 1


# Closing the previously opened file
f_name_opened.close()


# Displaying the RESULTS
print("***** LETTERS FREQUENCY *****")
smallest_letter = " "
smallest_words = min(letter_to_words.values())
for k in sorted(letter_to_words):
    print(k + " : " + str(letter_to_words[k]))
    if letter_to_words[k] == smallest_words:
        smallest_letter += k + " "
print("The LETTER that is used in the SMALLEST proportion of the words is ({}) -> {} words".format(
    smallest_letter, smallest_words))
