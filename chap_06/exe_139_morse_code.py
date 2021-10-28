"""
Morse code is an encoding scheme that uses dashes and dots to represent digits and letters.
In this exercise, you will write a program that uses a dictionary to store the mapping
from these symbols to Morse code.

Use a period to represent a dot, and a hyphen to represent a dash.
The mapping from characters to dashes and dots is shown in the Tables below:

    Character	        Code	            Character	        Code
        A	            . _	                    N	             _ .
        B	            _ . . .	                O	            _ _ _
        C	            _ . _ .	                P	            . _ _ .
        D	            _ . .	                Q	            _ _ . _
        E	            .	                    R	            . _ .
        F	            . . _ .	                S	            . . .
        G	            _ _ .	                T	            _
        H	            . . . .	                U	            . . _
        I	            . .	                    V	            . . . _
        J	            . _ _ _	                W	            . _ _
        K	            _ . _	                X	            _ . . _
        L	            . _ . .	                Y	            _ . _ _
        M	            _ _	                    Z	            _ _ . .

      Numbers	         Code	                 Numbers	            Code
        1	            . _ _ _ _	                6	              _ . . . .
        2	            . . _ _ _	                7	              _ _ . . .
        3	            . . . _ _	                8	              _ _ _ . .
        4	            . . . . _	                9	              _ _ _ _ .
        5	            . . . . .	                0	              _ _ _ _ _

    Character	        Code	                Character	            Code
        Á	            . _ _ . _	                Ä	                . _ . _
        É	            . . _ . .	                Ñ	                _ _ . _ _
        Ö	            _ _ _ .	                    Ü	                . . _ _


Your program should read a message from the user.
Then it should translate all of the letters and digits in the message to Morse code,
leaving a space between each sequence of dashes and dots.
Your program should ignore any characters that are not listed in the previous table.

The Morse code for Hello, World! is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..
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
