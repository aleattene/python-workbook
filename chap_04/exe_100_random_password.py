"""
Write a function that generates a random password.
The password should have a random length of between 7 and 10 characters.
Each character should be randomly selected from positions 33 to 126 in the ASCII table.
Your function will not take any parameters.
It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program.
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
