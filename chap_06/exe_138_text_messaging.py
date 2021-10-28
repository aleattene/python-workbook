"""
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are needed for most letters.
Pressing the number once generates the first character listed for that key.
Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character.

    Key	        Symbols
     1	         .,?!:
     2	          ABC
     3	          DEF
     4	          GHI
     5	          JKL
     6	          MNO
     7	          PQRS
     8	          TUV
     9	          WXYZ
     0	          space

Write a program that displays the key presses needed for a message entered by the user.
Construct a dictionary that maps from each letter or symbol to the key presses needed to generate it.
Then use the dictionary to create and display the presses needed for the user’s message.

For example:
- if the user enters Hello, World! then
- your program should output 4433555555666110966677755531111.

Ensure that your program handles both uppercase and lowercase letters.
Ignore any characters that aren’t listed in the table above such as semicolons and parentheses.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY -> valid characters
    pass


def symbolsToKey(key_symbols, text_message):
    # LIST of the KEY PRESSES NEEDED for the MESSAGE entered by the USER
    keys_mapped = []
    # Analysis of each character of the text message
    for char in text_message:
        # Analysis of each key within the dictionary
        for k in key_symbols:
            # Evaluation if char of the text message is inside a list (values in the dictionary)
            if char.upper() in key_symbols[k]:
                for i in range(len(key_symbols[k])):
                    # Evaluation key presses needed (alias -> index + 1)
                    if char.upper() == key_symbols[k][i]:
                        keys_mapped.append(str(k)*(i+1))
    return keys_mapped


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # DICTIONARY - KEY and SYMBOLS
    key_symbols = {
        1: [".", ",", "?", "!", ":"],
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"],
        5: ["J", "K", "L"],
        6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"],
        8: ["T", "U", "V"],
        9: ["W", "X", "Y", "Z"],
        0: [" "]
    }

    # Acquisition of DATA entered by the USER
    text_message = input("Enter the TEXT MESSAGE: ")
    # STRING TESTING
    # text_message = "Hello, World!"

    # Mapping SYMBOLS -> KEY PRESSES NEEDED
    keys = symbolsToKey(key_symbols, text_message)

    # Displaying the RESULT
    print("KEY PRESSES NEEDED for a MESSAGE ENTERED by the USER -> ", end="")
    for k in keys:
        print(k, end="")


if __name__ == "__main__":
    main()
