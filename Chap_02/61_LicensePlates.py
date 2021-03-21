"""
The program receives from the USER a STRING of CHARACTERS
and evaluates (displaying the results) if this STRING 
is VALID or NOT, for an OLDER STYLE license plate or a NEWER STYLE. 
"""

# START Definition of FUNCTIONS


def licensePlateValid(licensePlate):
    if 6 <= len(licensePlate) <= 7:
        return True
    return False


def checkLicensePlate(licensePlate):

    if len(licensePlate) == 6:
        for char in licensePlate[:3]:
            if ord(char) < 65 or ord(char) > 90:
                return "NOT VALID for one STYLE (OLDER or NEWER) of LICENSE PLATE."
        if not(licensePlate[3:].isdigit()):
            return "NOT VALID for one STYLE (OLDER or NEWER) of LICENSE PLATE."
        return "VALID for an \"OLDER\" STYLE LICENSE PLATE"

    if len(licensePlate) == 7:
        if not(licensePlate[:4].isdigit()):
            return "NOT VALID for one STYLE (OLDER or NEWER) of LICENSE PLATE."
        for char in licensePlate[4:]:
            if ord(char) < 65 or ord(char) > 90:
                return "NOT VALID for one STYLE (OLDER or NEWER) of LICENSE PLATE."
        return "VALID for a \"NEWER\" STYLE LICENSE PLATE"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
licensePlate = input("Enter the LICENSE PLATE (min 6 - max 7 characters): ")
licensePlateValidated = licensePlateValid(licensePlate)

while not(licensePlateValidated):
    print("Incorrect entry. Try again.")
    licensePlate = input(
        "Enter the LICENSE PLATE (min 6 - max 7 characters): ")
    licensePlateValidated = licensePlateValid(licensePlate)


# LICENSE PLATE evaluation
licensePlateChecked = checkLicensePlate(licensePlate)


# Displaying the RESULTS
print("The LICENSE PLATE \"" + licensePlate + "\" is " + licensePlateChecked)
