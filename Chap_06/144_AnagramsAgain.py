"""
The program receives TWO WORDS from the USER
and returns (displaying it) whether or not THEY are ANAGRAMS,
ignoring CAPITALIZATION, PUNCTUATION MARKS and SPACING.
"""


# START Definition of the FUNCTION


def checkAnagrams(word_1, word_2):
    # Dictionary of occurrences of strings characters
    chars_occurrences = {}
    # Dictionary population (with chars of the FIRST string)
    for char in word_1.lower():
        if "a" <= char <= "z" or char.isdigit():
            if char in chars_occurrences:
                chars_occurrences[char] += 1
            else:
                chars_occurrences[char] = 1
        else:  # improves code readability
            continue
    # Emptying dictionary (with chars of the SECOND string)
    for char in word_2.lower():
        if "a" <= char <= "z" or char.isdigit():
            if char in chars_occurrences:
                chars_occurrences[char] -= 1
                if chars_occurrences[char] == 0:
                    del chars_occurrences[char]
            else:
                return False
        else:  # improves code readability
            continue
    if len(chars_occurrences) > 0:
        return False
    else:  # EMPTY DICTIONARY (the two words are ANAGRAMS)
        return True


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    word_1 = input("Enter the FIRST word: ")
    word_2 = input("Enter the SECOND word: ")
    # STRING TESTING
    # word_1 = "William Shakespeare"
    # word_2 = "I am a weakish speller"

    # String evaluation (anagrams or not)
    anagrams = checkAnagrams(word_1, word_2)

    # Displaying the RESULTS
    if anagrams:
        result = "ARE"
    else:
        result = "ARE NOT"
    print("The two words \"{}\" and \"{}\" {} ANAGRAMS ".format(
        word_1, word_2, result), end="")
    print("(ignoring capitalization, punctuation marks and spacing).")


if __name__ == "__main__":
    main()
