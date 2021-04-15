"""
The program receives a TEXT MESSAGE from the USER
and returns (displaying it) the same message 
ENCODED using MORSE CODE.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY -> valid characters
    pass


def characterToMorseCode(text_message):
    # DICTIONARY - MORSE CODE
    morse_code = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "---..",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }
    # ENCODED MESSAGE
    encoded_message = ""
    # Analysis of each character of the text message
    for char in text_message:
        # Analysis of each key within the dictionary
        for k in morse_code:
            # Evaluation if the character of the text message is equal to a dictionary key
            if char.upper() == k:
                encoded_message += morse_code[k] + " "
    return encoded_message


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    text_message = input("Enter the TEXT MESSAGE: ")
    # STRING TESTING
    # text_message = "Hello, World!"

    # ENCODED MESSAGE
    encoded_message = characterToMorseCode(text_message)

    # Displaying the ENCODED MESSAGE
    print("MESSAGE ENTERED by the USER -> {}".format(text_message))
    print("ENCODED MESSAGE using MORSE CODE -> {}".format(encoded_message))


if __name__ == "__main__":
    main()
