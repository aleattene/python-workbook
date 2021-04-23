"""
The program identifies the LONGEST WORD(S) in a FILE 
(whose NAME is provided as a COMMAND-LINE ARGUMENT)
and displays ALL of the WORDS(S) of that LENGTH present in the file itself
(CATCHING and HANDLING any EXCEPTIONS)
"""

# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys

try:
    if len(sys.argv) != 2:
        raise Exception

    # Opening the file name (sysargv[1]) in read mode
    with open(sys.argv[1], "r") as f_name_opened:

        # Declaration of a VARIABLE and a LIST
        length_longest_word = 0
        longest_words = []

        # Select of the each Line from LIST of the LINES (returned from the readlines)
        for line in f_name_opened.readlines():
            # Select of the each WORD from LIST of the Words of each line
            for word in line.split():
                # WORD of equal length of the longest word
                if len(word) == length_longest_word:
                    longest_words.append(word)
                # WORD of greater length than the longest word
                elif len(word) > length_longest_word:
                    length_longest_word = len(word)
                    longest_words = []
                    longest_words.append(word)

    # Displaying the RESULTS
    print("The LENGTH of the LONGEST WORD present in the file \"{}\" is ({}) characters.". format(
        sys.argv[1], length_longest_word))
    if len(longest_words) == 1:
        print("The word that have this length is: ")
    else:
        print("The words that have this length are: ")
    for word in longest_words:
        print("- " + word)


# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[1]))
    quit()
# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()
