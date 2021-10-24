"""
The Program receives from the USER a NUMBER of SIDES (assumed as equal)
and returns (displaying it) the NAME of the represented SHAPE.
"""

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if 3 <= int(numero) <= 10:
            return True
    return False


def regularPolygon(numberSides):
    if valutaIntPositive(numberSides):
        polygons = {"3": "TRIANGLE", "4": "SQUARE", "5": "PENTAGON",
                    "6": "EXAGON", "7": "HEPTAGON", "8": "OCTAGON",
                    "9": "ENNAGON", "10": "DECAGON"}
        polygon = polygons[numberSides]
        return polygon


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
numberSides = input("Enter the NUMBER of SIDES (min 3 - max 10): ")
numberSidesValidated = valutaIntPositive(numberSides)

while not(numberSidesValidated):
    print("Incorrect entry. Try again.")
    numberSides = input("Enter the NUMBER of SIDES (min 3 - max 10): ")
    numberSidesValidated = valutaIntPositive(numberSides)


# REGULAR POLYGON Evaluation
polygon = regularPolygon(numberSides)


# Displaying the RESULTS
print("REGULAR POLYGON = " + polygon + " ( " + numberSides + " sides )")
