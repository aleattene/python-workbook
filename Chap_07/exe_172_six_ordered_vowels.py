"""
The program READS a FILE (whose NAME is provided by the USER) containing a LIST of WORDS 
and displays all of the words that contain EACH of the VOWELS (A, E, I, O, U, Y) 
exactly ONCE and in ORDER.
"""


open_file = True
while open_file:
    # Acquisition and Control of the DATA entered by the USER
    file_to_open = input(
        "Enter the file name containing the list of the words: ")
    # TESTING
    # file_to_open = "words.txt"
    # Opening the file in reading mode
    try:
        f_name_opened = open(file_to_open, "r")
        open_file = False
    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(file_to_open))


# String containing the ordered list of vowels
expected_vowels = "aeiouy"

# Select of the each Line from LIST of the LINES (returned from the readlines)
for word in f_name_opened.readlines():
    # String which will contain the real order of the vowels in the words that we will analyze
    vowels_in_word = ""
    for char in word.strip():
        if char.lower() in expected_vowels:
            vowels_in_word += char.lower()
    # Matching between the order of expected and real vowels
    if vowels_in_word == expected_vowels:
        print(word.strip())
        # possible evolution -> store words before and then display them

# Closing the previously opened file
f_name_opened.close()
