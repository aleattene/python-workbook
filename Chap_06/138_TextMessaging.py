"""
The program receives a TEXT MESSAGE from the USER
and returns (displaying it) the KEY PRESSES NEEDED for writing the same MESSAGE, 
using the numeric keypad of an older basic cellphone.
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
