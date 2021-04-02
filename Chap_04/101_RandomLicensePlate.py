"""
The program GENERATES and DISPLAYS a RANDOM LICENSE PLATE, considering that:
- OLD pattern of the license plates consist of THREE LETTERS followed by THREE DIGITS
- NEW pattern of the license plates consist of FOUR DIGITS followed by THREE LETTERS
"""

# IMPORT module RANDOM
import random as rd


# START Definition of the FUNCTIONS


def generateLicensePlate():
    new_old = rd.randint(0, 1)
    if new_old == 1:
        new = []
        for i in range(1, 5):
            new.append(chr(rd.randint(48, 57)))
        for i in range(1, 4):
            new.append(chr(rd.randint(65, 90)))
        license_plate = "".join(new)
    else:   # new_old == 0
        old = []
        for i in range(1, 4):
            old.append(chr(rd.randint(65, 90)))
        for i in range(1, 4):
            old.append(chr(rd.randint(48, 57)))
        license_plate = "".join(old)
    return license_plate


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # LICENSE PLATE generation and PATTERN evaluation
    license_plate = generateLicensePlate()
    if license_plate[0].isdigit():
        pattern = "new"
    else:
        pattern = "old"

    # LICENSE PLATE display
    print("LICENSE PLATE GENERATED -> {} ({} pattern)".format(license_plate, pattern))


if __name__ == "__main__":
    main()
