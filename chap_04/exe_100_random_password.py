"""
The program GENERATES and DISPLAYS a RANDOM PASSWORD:
- having a random length between 7 and 10 characters
- with each character randomly selected 
    between position 33 and 126 of the ASCII table.
"""

# IMPORT module RANDOM
import random as rd


# START Definition of the FUNCTIONS


def generatePassword():
    lenght_pwd = rd.randint(7, 10)
    pwd_temp = []
    for i in range(lenght_pwd):
        character = chr(rd.randint(33, 126))
        pwd_temp.append(character)
    pwd = "".join(pwd_temp)
    return pwd


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # PASSWORD generation
    pwd = generatePassword()

    # PASSWORD display
    print("PASSWORD GENERATED -> {} (length {} characters)".format(pwd, len(pwd)))


if __name__ == "__main__":
    main()
