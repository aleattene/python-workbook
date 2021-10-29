"""
The program receives a WORD from the USER 
and displays whether or not it is a PALINDROME.
"""


# START Definition of FUNCTION

def checkPalindrome(word):
    # BASE CASE (empty word or unique char)
    if len(word) < 2:
        return True
    # RECURSIVE CASES (each recursive case remove first char and last char of the tail)
    tail = word[1:-1]
    # Check if the first character matches with the last character
    if word[0] == word[-1]:
        return True and checkPalindrome(tail)
    else:
        return False


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of the WORD entered by the USER
    word = input("Enter a WORD: ")

    # String evaluation (is a PALINDROME or not)
    word_palindrome = checkPalindrome(word)

    # Displaying the RESULT
    if word_palindrome:
        result = "IS"
    else:
        result = "IS NOT"
    print("The word \"{}\" {} a PALINDROME.".format(word, result))


if __name__ == "__main__":
    main()
