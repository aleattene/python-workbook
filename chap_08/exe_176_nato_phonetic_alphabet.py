"""
The program receives a WORD from the USER 
and displays its PHONETIC SPELLING.
"""


# START Definition of FUNCTION


def phoneticSpelling(word):
    # DICTIONARY
    NATO_phonetic_spelling = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu"
    }
    # BASE CASE (empty word)
    if word == "":
        return ""
    # RECURSIVE CASES (each recursive case remove first char of the tail)
    tail = word[1:len(word)]
    # Check character presence in the dictionary
    if word[0].upper() in NATO_phonetic_spelling:
        # Char PRESENT
        return NATO_phonetic_spelling[word[0].upper()] + " " + phoneticSpelling(tail)
    else:  # Char NOT PRESENT
        return phoneticSpelling(tail) + " "


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of the WORD entered by the USER
    word = input("Enter the WORD: ")

    # WORD -> Phonetic Spelling
    word_spelling = phoneticSpelling(word)

    # Displaying the RESULT
    print("{} -> {}".format(word.upper(), word_spelling))


if __name__ == "__main__":
    main()
