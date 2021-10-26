"""
The program receives from the USER
the LENGTHS of the TWO SHORTER SIDES of a RIGHT TRIANGLE
and returns (displaying it) its HYPOTENUSE
(computed using Pythagorean Theorem).
"""

# IMPORT MATH module
import math


# START Definition of FUNCTIONS

def valutaEntry(number):
    # Check Entry -> INT or FLOAT POSITIVE
    return True


def sidesToHypotenuse(side_1, side2):
    # Pythagorean Theorem
    hypotenuse = math.sqrt((side_1) ** 2 + (side_2) ** 2)
    return hypotenuse


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
side_1 = input("Enter the FIRST SHORT SIDE of the RIGHT TRIANGLE: ")
side_1_validated = valutaEntry(side_1)
side_2 = input("Enter the SECOND SHORT SIDE of the RIGHT TRIANGLE: ")
side_2_validated = valutaEntry(side_2)

while not(side_1_validated and side_2_validated):
    print("Incorrect entry. Try again.")
    side_1 = input("Enter the FIRST SHORT SIDE of the RIGHT TRIANGLE: ")
    side_1_validated = valutaEntry(side_1)
    side_2 = input("Enter the SECOND SHORT SIDE of the RIGHT TRIANGLE: ")
    side_2_validated = valutaEntry(side_2)


# SIDES conversion : STR -> FLOAT
side_1 = float(side_1)
side_2 = float(side_2)


# Computing the HYPOTENUSE of the RIGHT TRIANGLE
hypotenuse = sidesToHypotenuse(side_1, side_2)


# Displaying the RESULT
print("The HYPOTENUSE of the RIGHT TRIANGLE (having the first short side equal to %.2f" % side_1 +
      " and the second short side equal to %.2f" % side_2 + ") is \"%.2f" % hypotenuse + "\".")
