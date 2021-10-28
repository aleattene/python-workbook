"""
Create a program that determines and displays the number of unique characters in a string entered by the user.

For example:
"Hello, World!" has 10 unique characters
while "zzz" has only one unique character.

Use a dictionary or set to solve this problem.
"""


# START Definition of the FUNCTION


def charsOccurrences(text_message):
    # DICTIONARY - Occurrences UNIQUE CHARACTERS
    chars_occurrences = {}
    # Analysis of the SINGLE CHAR of the TEXT MESSAGE
    for char in text_message:
        # Char already present in the dictionary
        if char in chars_occurrences:
            chars_occurrences[char] += 1
        # Char not present in the dictionary
        else:
            chars_occurrences[char] = 1
    return chars_occurrences


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    text_message = input("Enter the TEXT MESSAGE: ")
    # STRING TESTING
    # text_message = "Hello, World!"
    # text_message = "zzz"

    # COUNT of UNIQUE CHARS in the TEXT MESSAGE
    unique_chars_dict = charsOccurrences(text_message)
    unique_chars = len(unique_chars_dict)

    # Displaying the RESULT
    if unique_chars == 0:   # entered an empty message
        print("The TEXT MESSAGE entered by the USER does NOT CONTAIN characters.")
    else:
        if unique_chars == 1:  # entered only one unique character in the message
            result = "CONTAIN"
            char_chars = "character."
        else:
            result = "CONTAIN"
            char_chars = "characters."
        print("The TEXT MESSAGE entered by the USER {} {} {}".format(
            result, unique_chars, char_chars))


if __name__ == "__main__":
    main()
