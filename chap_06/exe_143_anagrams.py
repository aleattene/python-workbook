"""
Two words are anagrams if they contain all of the same letters, but in a different order.

For example:
“evil” and “live” are anagrams because each contains one “e”, one “i”, one “l”, and one “v”.

Create a program that reads two strings from the user,
determines whether or not they are anagrams, and
reports the result.
"""


# START Definition of the FUNCTION


def checkAnagrams(word_1, word_2):
    # Dictionary of occurrences of strings characters
    chars_occurrences = {}
    # Dictionary population (with chars of the FIRST string)
    for char in word_1:
        if char in chars_occurrences:
            chars_occurrences[char] += 1
        else:
            chars_occurrences[char] = 1
    # Emptying dictionary (with chars of the SECOND string)
    for char in word_2:
        if char in chars_occurrences:
            chars_occurrences[char] -= 1
            if chars_occurrences[char] == 0:
                del chars_occurrences[char]
        else:
            return False
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
    # word_1 = "evil"
    # word_2 = "live"

    # String evaluation (anagrams or not)
    anagrams = checkAnagrams(word_1, word_2)

    # Displaying the RESULTS
    if anagrams:
        result = "ARE"
    else:
        result = "ARE NOT"
    print("The two words \"{}\" and \"{}\" {} ANAGRAMS.".format(
        word_1, word_2, result))


if __name__ == "__main__":
    main()
