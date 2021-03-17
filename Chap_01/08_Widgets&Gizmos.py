"""
The program REQUIRES the USER to enter the WIDGETS NUMBER and the GIZMOS NUMBER.
Afterward, it displays the PARTIAL and TOTAL WEIGHTS of objects, considering that:
- Weight WIDGET = 75 grams
- Weight GIZMO = 112 grams
"""

# Declaration of VARIABLES / CONSTANTS
WEIGHT_WIDGET = 75      # Weight WIDGET = 75 grams
WEIGHT_GIZMO = 112      # Weight GIZMO = 112 grams

# Acquisition and Control of the DATA entered by the USER
widgets = input("How many WIDGETS do you have to weigh? ")
gizmos = input("And how many GIZMOS? ")

while not(widgets.isdigit()) or not(gizmos.isdigit()):
    print("Incorrect entry. Try again by entering integer for both requests")
    widgets = input("How many WIDGETS do you have to weigh? ")
    gizmos = input("And how many GIZMOS? ")


# Computing of PARTIAL and TOTAL WEIGHTS
weightWidgets = WEIGHT_WIDGET * int(widgets)
weightGizmos = WEIGHT_GIZMO * int(gizmos)
totalWeight = weightWidgets + weightGizmos

# Displaying the RESULTS
print("Weight Widgets = %i" % weightWidgets + " grams")
print("Weight Gizmos = %i" % weightGizmos + " grams")
print("TOTAL Weight = %i" % totalWeight + " grams")
