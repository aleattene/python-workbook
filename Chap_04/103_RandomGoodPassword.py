"""
The program GENERATES and DISPLAYS RANDOM PASSWORDS 
until generates a GOOD PASSWORD, that is:
- long AT LEAST 8 characters
- containing AT LEAST one UPPERCASE letter, one LOWERCASE letter and one NUMBER.
"""

# IMPORT module RANDOM
import random as rd


# START Definition of the FUNCTIONS


def generatePassword():                 # Possibile evolution -> import module
    lenght_pwd = rd.randint(7, 10)
    pwd_temp = []
    for i in range(lenght_pwd):
        character = chr(rd.randint(33, 126))
        pwd_temp.append(character)
    pwd = "".join(pwd_temp)
    return pwd


def goodPassword(password):              # Possibile evolution -> import module
    if len(password) < 8:
        return False
    letter_upper = 0
    letter_lower = 0
    number = 0
    for i in range(len(password)):
        if "A" <= password[i] <= "Z":
            letter_upper += 1
        elif "a" <= password[i] <= "z":
            letter_lower += 1
        elif "0" <= password[i] <= "9":
            number += 1
        elif password[i] == " ":
            return False
    if (letter_upper >= 1 and letter_lower >= 1 and number >= 1):
        return True
    else:
        return False


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Declaration of VARIABLES
    attempt = 1
    good_password = False

    # Generation and checking of a GOOD PASSWORD
    while not(good_password):
        print("Attempt n. {:02d}".format(attempt))
        pwd = generatePassword()
        # PASSWORD display
        print("PASSWORD GENERATED -> {} (length {} characters) -> ".format(pwd,
                                                                           len(pwd)), end="")
        # PASSWORD check
        good_password = goodPassword(pwd)
        if good_password:
            print("IS a GOOD PASSWORD.")
        else:
            print("is not a good password.")
        attempt += 1


if __name__ == "__main__":
    main()
