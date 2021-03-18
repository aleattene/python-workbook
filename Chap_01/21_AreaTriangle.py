""" 
The Program receives from the USER, BASE and HEIGHT of a triangle
and calculates its AREA.
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


def areaTriangle(base, height):
    area = (base * height) / 2
    return area


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the BASE and HEIGHT of the TRIANGLE.")
base = input("BASE (cm): ")
height = input("HEIGHT (cm): ")

baseFloatPositive = valutaFloatPositive(base)
heightFloatPositive = valutaFloatPositive(height)
baseIntPositive = valutaIntPositive(base)
heightIntPositive = valutaIntPositive(height)

while not(baseIntPositive or baseFloatPositive) or \
    not(heightIntPositive or heightFloatPositive):
    print("Incorrect entry. Try again.")   
    print("Enter the BASE and HEIGHT of the TRIANGLE.")
    base = input("BASE (cm): ")
    height = input("HEIGHT (cm): ")

    baseFloatPositive = valutaFloatPositive(base)
    heightFloatPositive = valutaFloatPositive(height)
    baseIntPositive = valutaIntPositive(base)
    heightIntPositive = valutaIntPositive(height)


# Conversion STR -> FLOAT
base = float(base)
height = float(height)


# Computing of the TRIANGLE AREA
area = areaTriangle(base, height)                    

# Displaying the RESULT
print("AREA of the TRIANGLE = %.2f" % area + " square centimeters")
