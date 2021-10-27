"""
In this exercise, you will create a program that reads words from the user until the user enters a blank line.
After the user enters a blank line your program should display each word entered by the user exactly once.
The words should be displayed in the same order that they were first entered.

For example, if the user enters:

first second first third second

then your program should display:

first second third
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
