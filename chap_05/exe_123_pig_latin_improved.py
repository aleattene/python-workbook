"""
The program extends exercise 122 (file 122_PingLatin),
so that CAPITAL LETTERS and PUNCTUATION MARKS
(commas, points, question marks, and exclamation marks) are correctly managed:
- if a word begins with a CAPITAL letter,
    its PIG LATIN representation should begin anyway with a capital letter
    and the shifted letter to the end of the word
    should be changed to lowercase (Computer -> Omputercay)
- if a word ends with a PUNCTUATION MARKS,
    the punctuation mark it should remain at the end of the word
    after the transformation has been performed (Science! -> Iencescay!)
"""


# START Definition of the FUNCTION


def checkEntry(line_text):      # possible evolution -> check entry
    pass


# ["s","t","r","i","n","g","a","?","a","y"] -> ["s","t","r","i","n","g","a","a","y","?"]
def punctuationManagement(list_chars):
    punctuation_marks = [".", ",", "?", "!"]
    marks = 0
    # WARNING -> edit the original caller list
    for i in range(len(list_chars)):
        if list_chars[i] in punctuation_marks:
            while list_chars[i] in punctuation_marks:
                list_chars.append(list_chars[i])
                list_chars.pop(i)
            return


def translateToPigLatin(strings_list):
    # WOLVELS
    wovels_lower = ["a", "e", "i", "o", "u"]
    wovels_upper = ["A", "E", "I", "O", "U"]
    # CONSONANTS
    consonants_lower = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
                        "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    consonants_upper = ["B", "C", "D", "F", "G", "H", "J", "K", "L",
                        "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    for i in range(len(strings_list)):
        # ["stringa"] -> ["a"] or ["A"]
        if strings_list[i][0] in wovels_lower or strings_list[i][0] in wovels_upper:
            # ["stringa"] -> ["s","t","r","i","n","g","a"]
            list_tmp = list(strings_list[i])
            if list_tmp[0] in wovels_upper:
                # ["a"] -> ["A"]
                list_tmp[0] = list_tmp[0].upper()
            # ["s","t","r","i","n","g","a","?"] -> ["s","t","r","i","n","g","a","?","w","a","y"] or
            # ["S","t","r","i","n","g","a","?"] -> ["S","t","r","i","n","g","a","?","w","a","y"]
            list_tmp.append("w")
            list_tmp.append("a")
            list_tmp.append("y")
            # ["s","t","r","i","n","g","a","?","w","a","y"] -> ["s","t","r","i","n","g","a","w","a","y","?"]
            punctuationManagement(list_tmp)
            # ["s","t","r","i","n","g","a","w","a","y"] -> ["Stringaway"] or
            # ["s","t","r","i","n","g","a","w","a","y","?"] -> ["Stringaway?"]
            strings_list[i] = "".join(list_tmp)
        # ["stringa"] -> ["s"] or ["S"]
        elif strings_list[i][0] in consonants_lower or strings_list[i][0] in consonants_upper:
            # ["stringa"] -> ["s","t","r","i","n","g","a"]
            list_tmp = list(strings_list[i])
            capitalize = False      # ["s"]
            if list_tmp[0] in consonants_upper:
                capitalize = True   # ["S"]
            while list_tmp[0] in consonants_lower or list_tmp[0] in consonants_upper:
                list_tmp.append(list_tmp[0].lower())
                list_tmp.pop(0)
            if capitalize:
                # ["s"] -> ["S"]
                list_tmp[0] = list_tmp[0].upper()
            # ["s","t","r","i","n","g","a","?","a","y"] -> ["s","t","r","i","n","g","a","a","y","?"] or
            # ["S","t","r","i","n","g","a","?","a","y"] -> ["S","t","r","i","n","g","a","a","y","?"]
            list_tmp.append("a")
            list_tmp.append("y")
            # ["s","t","r","i","n","g","a","?","a","y"] -> ["s","t","r","i","n","g","a","a","y","?"]
            punctuationManagement(list_tmp)
            # ["s","t","r","i","n","g","a","a","y"] -> ["stringaay"] or
            # ["s","t","r","i","n","g","a","a","y","?"] -> ["stringaay?"]
            strings_list[i] = "".join(list_tmp)
    return strings_list


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    text = input("Enter the TEXT: ")
    # STRING TESTING
    # text = "computer, think? algorithm! office."

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
