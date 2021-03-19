"""
The Program receives a WORD from the USER 
and Display for EACH CHARACTER that composes it,
if it represents a VOWEL or a CONSONANT.
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
    print(char + " = " + result)
