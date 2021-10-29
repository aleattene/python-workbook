"""
Write a program that reads values from the user until a blank line is entered.
Display the total of all of the values entered by the user (or 0.0 if the first value entered is a blank line).

Complete this task using recursion.

Your program may not use any loops.

Hint: The body of your recursive function will need to read one value from the user, and then
determine whether or not to make a recursive call.
Your function does not need to take any arguments, but it will need to return a numeric result.
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
