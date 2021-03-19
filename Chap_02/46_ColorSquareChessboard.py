""" 
The program receives from the USER one POSITION of the CHESSBOARD
and displays the COLOR of that POSITION (BLACK or WHITE)
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


# Acquisition and Control of the DATA entered by the USE
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
