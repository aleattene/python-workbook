"""
The program receives from the USER the LENGTH of the THREE STRAWS
and returns (displaying it) if is POSSIBLE or NOT,
use them to CREATE a valid (scalene, isosceles, equilateral) TRIANGLE.
"""


# START Definition of FUNCTIONS


def valutaEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INT or FLOAT (not negative)
    return True


def checkTriangle(side1, side2, side3):
    if side1 == 0 or side2 == 0 or side3 == 0:
        return False
    else:
        # VALID TRIANGLE RULE -> EACH SIDE must always be greater than the difference of the other two
        # Alternative -> EACH SIDE must always be less than the sum of the other two
        if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side2 + side1):
            return False
    return True


def typeTriangle(side1, side2, side3):
    if side1 == side2:
        if side2 == side3:
            return "an EQUILATERAL(three equal sides)"
        return "an ISOSCELES(two equal sides)"
    elif side1 == side3:
        if side3 == side2:
            return "an EQUILATERAL(three equal sides)"
        return "an ISOSCELES(two equal sides)"
    elif side2 == side3:
        if side3 == side1:
            return "an EQUILATERAL(three equal sides)"
        return "an ISOSCELES(two equal sides)"
    else:
        return "a SCALENE(all different sides)"


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

   # Acquisition and Control of the DATA entered by the USER
    print("Enter the LENGTH of the THREE STRAWS.")
    side1 = input("STRAW 1: ")
    side2 = input("STRAW 2: ")
    side3 = input("STRAW 3: ")
    side1_validated = valutaEntry(side1)
    side2_validated = valutaEntry(side2)
    side3_validated = valutaEntry(side3)

    while not(side1_validated and side2_validated and side3_validated):
        print("Incorrect entry. Try again.")
        print("Enter the LENGTH of the THREE STRAWS.")
        side1 = input("STRAW 1: ")
        side2 = input("STRAW 2: ")
        side3 = input("STRAW 3: ")
        side1_validated = valutaEntry(side1)
        side2_validated = valutaEntry(side2)
        side3_validated = valutaEntry(side3)

    # Conversion STR -> FLOAT
    side1 = int(side1)
    side2 = int(side2)
    side3 = int(side3)

    # VALIDITY TRIANGLE computing
    valid_triangle = checkTriangle(side1, side2, side3)

    # Displaying the RESULTS
    print("With the THREE entered STRAWS", end="")
    if valid_triangle:
        print(" it is POSSIBLE to CREATE " +
              typeTriangle(side1, side2, side3) + " TRIANGLE.")
    else:
        print(" it is NOT POSSIBLE to CREATE a TRIANGLE.")


if __name__ == "__main__":
    main()
