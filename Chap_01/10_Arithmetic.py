"""
The Program receives from the USER TWO INTEGERS and 
returns (displaying) SUM, DIFFERENCE, PRODUCT, DIVISION
(with quotient and remainder), LOGARITHM and POWER ELEVATION.
"""

# IMPORT Module MATH
import math

# Start Definition of FUNCTIONS


def somma(a, b):
    return a + b


def difference(a, b):
    if a >= b:
        return a - b


def product(a, b):
    return a * b


def quotient(a, b):
    if b != 0:
        return a / b
    else:
        return 0  # Impossible Division


def remainder(a, b):
    if b != 0:
        return a % b
    else:
        return 0  # Impossible Division


def logarithm(a):
    return float(math.log10(a))


def potenza(a, b):
    return a ** b   # Alternative option -> math.pow(a,b)

# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
a = int(input("Enter the FIRST NUMBER: "))
b = int(input("Enter the SECOND NUMBER (less than %i" %
              a + " and different from zero): "))

# Computing the RESULTS
resultSomma = somma(a, b)
resultDifferenza = difference(a, b)
resultProdotto = product(a, b)
resultQuoziente = quotient(a, b)
resultResto = remainder(a, b)
resultLogaritmo = logarithm(a)
resultPotenza = potenza(a, b)

# Displaying the RESULTS
print("The SUM between %i" % a + " and %i" % b + " is %i" % resultSomma)
print("The DIFFERENCE between %i" % a + " and %i" %
      b + " is %i" % resultDifferenza)
print("The PRODUCT between %i" % a + " and %i" % b + " is %i" % resultProdotto)
print("The QUOTIENT of the division between %i" %
      a + " and %i" % b + " is %i" % resultQuoziente)
print("The REMAINDER of the division between %i" %
      a + " and %i" % b + " is %i" % resultResto)
print("The LOGARITHM (base 10) of %i" % a + " is %.2f" % resultLogaritmo)
print("The RESULT of %i" % a + " ** %i" % b + " is %i" % resultPotenza)
