"""
The program receives WORDS from the USER UNTIL the user inserts a BLANK LINE.
After that, the program displays EACH WORD entered by the USER 
EXACTLY ONCE, in the SAME ORDER that they were first ENTERED.
"""

# START MAIN PROGRAM


def main():

    # EMPTY list
    words = []

    # Acquisition and Control of the DATA entered by the USER
    word = input("Enter the WORD (blank line to quit): ")

    while word != "":
        if word not in words:
            words.append(word)
        word = input("Enter the WORD (blank line to quit): ")

    # Displaying the RESULTS
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
