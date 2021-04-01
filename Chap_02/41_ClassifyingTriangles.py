"""
the Program receives from the USER the LENGTH of the THREE SIDES of a TRIANGLE,
and returns (displaying it) the TYPE of TRIANGLE, knowing that:
- three equal sides -> EQUILATERAL triangle
- two equal sides -> ISOSCELES triangle
- three different sides -> SCALENE triangle.
"""

# START Definition of FUNCTIONS


def valutaFloatPositive(numero):
    countPoints = 0
    for char in numero:
        if ord(char) == 46:
            countPoints += 1
    if countPoints == 1 and numero != "." and valutaNumero(numero):
        if isinstance(float(numero), float) and float(numero) > 0:
            return True
    else:
        return False


def valutaNumero(numero):
    if numero == "":
        return False
    countSigns = 0
    for char in numero:
        if ord(char) == 45 or ord(char) == 43:
            countSigns += 1
    if ((numero[0] == "+") or (numero[0] == "-")) and countSigns == 1 and \
            numero != "-" and numero != "+" and numero != "-." and numero != "+.":
        return True
    elif numero[0].isdigit() and countSigns == 0:
        return True
    else:
        return False


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def verificaTriangle(side1, side2, side3):
    if side1 >= (side2 + side3):
        return False
    if side2 >= (side1 + side3):
        return False
    if side3 >= (side2 + side1):
        return False
    return True


def typeTriangle(side1, side2, side3):
    if side1 == side2:
        if side2 == side3:
            return "EQUILATERAL (three equal sides)"
        return "ISOSCELES (two equal sides)"
    elif side1 == side3:
        if side3 == side2:
            return "EQUILATERAL (three equal sides)"
        return "ISOSCELES (two equal sides)"
    elif side2 == side3:
        if side3 == side1:
            return "EQUILATERAL (three equal sides)"
        return "ISOSCELES (two equal sides)"
    else:
        return "SCALENE (all different sides)"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the THREE SIDES of the TRIANGLE.")
side1 = input("FIRST SIDE (cm): ")
side2 = input("SECOND SIDE (cm): ")
side3 = input("THIRD SIDE (cm): ")
side1FloatPositive = valutaFloatPositive(side1)
side1IntPositive = valutaIntPositive(side1)
side2FloatPositive = valutaFloatPositive(side2)
side2IntPositive = valutaIntPositive(side2)
side3FloatPositive = valutaFloatPositive(side3)
side3IntPositive = valutaIntPositive(side3)

while not(side1IntPositive or side1FloatPositive) or \
    not(side2IntPositive or side2FloatPositive) or \
        not(side3IntPositive or side3FloatPositive):
    print("Incorrect entry. Try again.")
    print("Enter the THREE SIDES of the TRIANGLE.")
    side1 = input("FIRST SIDE (cm): ")
    side2 = input("SECOND SIDE (cm): ")
    side3 = input("THIRD SIDE (cm): ")

    side1FloatPositive = valutaFloatPositive(side1)
    side1IntPositive = valutaIntPositive(side1)
    side2FloatPositive = valutaFloatPositive(side2)
    side2IntPositive = valutaIntPositive(side2)
    side3FloatPositive = valutaFloatPositive(side3)
    side3IntPositive = valutaIntPositive(side3)


# Conversion STR -> FLOAT
side1 = float(side1)
side2 = float(side2)
side3 = float(side3)


# verification of the EXISTENCE of the TRIANGLE
if (side1IntPositive or side1FloatPositive) and \
    (side2IntPositive or side2FloatPositive) and \
        (side3IntPositive or side3FloatPositive):
    triangoloVerified = verificaTriangle(side1, side2, side3)

while not(triangoloVerified):
    print("ATTENTION: the SUM of TWO SIDES cannot be greater than the THIRD." +
          "THIS TRIANGLE does NOT EXISTS. Try Again.")
    print("Enter the THREE SIDES of the TRIANGLE.")
    side1 = input("FIRST SIDE (cm): ")
    side2 = input("SECOND SIDE (cm): ")
    side3 = input("THIRD SIDE (cm): ")

    side1FloatPositive = valutaFloatPositive(side1)
    side1IntPositive = valutaIntPositive(side1)
    side2FloatPositive = valutaFloatPositive(side2)
    side2IntPositive = valutaIntPositive(side2)
    side3FloatPositive = valutaFloatPositive(side3)
    side3IntPositive = valutaIntPositive(side3)
    if (side1IntPositive or side1FloatPositive) and \
        (side2IntPositive or side2FloatPositive) and \
            (side3IntPositive or side3FloatPositive):
        side1 = float(side1)
        side2 = float(side2)
        side3 = float(side3)
        triangoloVerified = verificaTriangle(side1, side2, side3)


# Identification of the TRIANGLE TYPE
typeTriangle = typeTriangle(side1, side2, side3)


# Displaying the RESULT
print("TYPE of TRIANGLE = " + typeTriangle)
