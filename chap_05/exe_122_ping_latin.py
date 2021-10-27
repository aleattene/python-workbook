"""
Pig Latin is a language constructed by transforming English words.
While the origins of the language are unknown,
it is mentioned in at least two documents from the nineteenth century,
suggesting that it has existed for more than 100 years.

The following rules are used to translate English into Pig Latin:
- if the word begins with a consonant (includingy), then
    all letters at the beginning of the word,
    up to the first vowel (excluding y),
    are removed and then
    added to the end of the word,
    followed by ay.
    For example:
        computer becomes omputercay and think becomes inkthay.
- if the word begins with a vowel (not including y), then
    way is added to the end of the word.
    For example:
        algorithm becomes algorithmway and office becomes officeway.

Write a program that reads a line of text from the user.
Then your program should translate the line into Pig Latin and display the result.
You may assume that the string entered by the user only contains lowercase letters and spaces.
"""


# START Definition of the FUNCTION


def checkEntry(line_text):      # possible evolution -> check entry
    pass


def translateToPigLatin(strings_list):
    wovels_lower = ["a", "e", "i", "o", "u"]
    consonants_lower = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
                        "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    for i in range(len(strings_list)):
        # ["stringa"] -> ["s"]
        if strings_list[i][0] in wovels_lower:
            strings_list[i] += "way"    # ["stringa"] -> ["stringaway"]
        elif strings_list[i][0] in consonants_lower:
            # ["stringa"] -> ["s","t","r","i","n","g","a"]
            list_tmp = list(strings_list[i])
            while list_tmp[0] in consonants_lower:
                list_tmp.append(list_tmp[0])
                list_tmp.pop(0)
            # ["s","t","r","i","n","g","a"] -> ["stringaay"]
            strings_list[i] = "".join(list_tmp) + "ay"
    return strings_list


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    text = input("Enter the TEXT: ")
    # STRING TESTING
    # text = "computer think algorithm office"

    # ORIGINAL LIST generation -> ["string","string"]
    original_strings_list = text.split()

    # TRANSLATED (PIG LATIN) LIST
    strings_translated = translateToPigLatin(original_strings_list)

    # Displaying the RESULTS
    print("ORIGINAL TEXT -> {}".format(text))
    print("TEXT TRANSLATED (PIG LATIN) -> ", end="")
    for string in strings_translated:
        print(string, end=" ")


if __name__ == "__main__":
    main()
