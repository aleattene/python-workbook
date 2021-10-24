"""
In this exercise you will create a program that reads a letter of the alphabet from the user.
If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a VOWEL.
If the user enters y then your program should display a message
indicating that sometimes y is a VOWEL, and sometimes y is a CONSONANT.
Otherwise your program should display a message indicating that the letter is a CONSONANT.
"""

# START Definition of FUNCTIONS


def stringaValida(stringInput):
    if stringInput != "":
        for char in stringInput:
            if not((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
                return False
        return True


def vowelOrConsonant(char):
    if char == "A" or char == "E" or char == "I" or char == "O" or \
            char == "U" or char == "a" or char == "e" or char == "i" or \
            char == "o" or char == "u":
        return "Vowel"
    elif char == "Y" or char == "y":
        return "Sometimes Vowel, sometimes Consonant"
    else:
        return "Consonant"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
stringInput = input("Enter the WORD: ")
stringInputValidated = stringaValida(stringInput)

while not(stringInputValidated):
    print("Incorrect entry. Try again.")
    stringInput = input("Enter the WORD: ")
    stringInputValidated = stringaValida(stringInput)


# Displaying the RESULTS
for char in stringInput:
    result = vowelOrConsonant(char)
    print(f'{char} = {result}')
