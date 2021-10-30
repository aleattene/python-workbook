"""
The program determines and displays the FREQUENCIES of all of the LETTERS
present in the FILE whose NAME is provided as a COMMAND-LINE ARGUMENT.
The program IGNORES spaces, punctuation marks, digits and is CASE-INSENSITIVE.
"""

# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys

try:
    if len(sys.argv) != 2:
        raise Exception

    # Opening the file name (sysargv[1]) in read mode
    with open(sys.argv[1], "r") as f_name_opened:

        # Declaration of the dictionary which will contain the frequency of the letters
        letters_frequency = {}

        # Select of the each Line from LIST of the LINES (returned from the readlines)
        for line in f_name_opened.readlines():
            # Select of the each char from each line
            for char in line:
                # The character is a letter (A-Z or a-z)
                if "A" <= char.upper() <= "Z":
                    # Letter already present in the dictionary -> frequency counter increment
                    if char.upper() in letters_frequency:
                        letters_frequency[char.upper()] += 1
                    else:
                        # Letter not present in the dictionary -> added new element
                        letters_frequency[char.upper()] = 1

    # Displaying the RESULTS
    print("***** FILE \"{}\" - LETTERS FREQUENCY *****".format(sys.argv[1]))
    for k in sorted(letters_frequency):
        print(k + " : " + str(letters_frequency[k]))
    print("***** END *****")


# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[1]))
    quit()
# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()
# Possible evolution -> handle generics exceptions in a manner more specific
