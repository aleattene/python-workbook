"""
The program receives from the USER a PASSWORD
and returns (displaying it) whether or not it is a GOOD PASSWORD, that is:
- long AT LEAST 8 characters
- containing AT LEAST one UPPERCASE letter, one LOWERCASE letter and one NUMBER.
"""


# START Definition of the FUNCTIONS


def goodPassword(password):
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

    # DATA acquisition (from USER)
    pwd = input("Enter the PASSWORD: ")

    # PASSWORD evaluation (good password or not)
    good_password = goodPassword(pwd)

    # Displaying the RESULT
    print("The password entered \"{}\" ".format(pwd), end="")
    if good_password:
        print("IS a GOOD PASSWORD.")
    else:
        print("IS NOT a GOOD PASSWORD.")


if __name__ == "__main__":
    main()
