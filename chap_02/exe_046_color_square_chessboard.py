"""
Positions on a chess board are identified by a letter and a number.
The letter identifies the column, while the number identifies the row.

Write a program that reads a position from the user.
Use an if statement to determine if the column begins with a black square or a white square.
Then use modular arithmetic to report the color of the square in that row.

For example, if the user enters a1 then your program should report that the square is black.
If the user enters d5 then your program should report that the square is white.
Your program may assume that a valid position will always be entered.
It does not need to perform any error checking.
"""

# START Definition of FUNCTIONS


def positionValida(position):
    if len(position) == 2:
        if 97 <= ord(position[0].lower()) <= 104:
            if 49 <= ord(position[1]) <= 56:
                return True
    return False


def positionToColorSquare(position):
    if (position[0].lower() == "a") or (position[0].lower() == "c") or \
        (position[0].lower() == "e") or (position[0].lower() == "g"):
        if int(position[1]) % 2 == 1:
            return "BLACK"
        else:
            return "WHITE"
    else:
        if int(position[1]) % 2 == 1:
            return "WHITE"
        else:
            return "BLACK"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
position = input(
    "Enter the POSITION in the CHESSBOARD (between \"a1\" and \"h8\"): ")
positionValidated = positionValida(position)

while not(positionValidated):
    print("Incorrect entry. Try again.")
    position = input(
        "Enter the POSITION in the CHESSBOARD (between \"a1\" and \"h8\"): ")
    positionValidated = positionValida(position)


# Identification POSITION -> COLOR
colorSquare = positionToColorSquare(position)


# Displaying the RESULTS
print("POSITION \"" + position + "\" -> COLOR \"" + colorSquare + "\"")
