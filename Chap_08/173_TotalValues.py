"""
The program receives VALUES from the USER (until a blank line is entered)
and returns (displaying it) the SUM of the VALUES entered
(it returns 0.0 if the first value entered is a blank line).
"""


# START Definition of the FUNCTION


def totalValues():
    # Acquisition of the VALUE entered by the USER
    value = input("Enter the VALUE (blank line to quit): ")
    # BASE CASE
    if value == "":
        return 0.0
    # RECURSIVE CASES
    else:
        return float(value) + totalValues()


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # FUNCTION CALL
    total_values = totalValues()

    # Displaying the RESULT
    print("Total VALUES = {}".format(total_values))


if __name__ == "__main__":
    main()
