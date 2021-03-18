"""
The Program receives from the USER your HEIGHT (in FEET and INCHES)
and converts it into CENTIMETERS.
"""

# Acquisition and Control of the DATA entered by the USER
print("Enter your HEIGHT (feet ad inches).")
heightFeet = input("How many FEET? ")
heightInches = input("And how many INCHES? ")

while not(heightFeet.isdigit() and heightFeet != "0") and \
        not(heightInches.isdigit() and heightInches != "0"):
    print("Incorrect entry. Try again.")
    print("Enter your HEIGHT (feet ad inches).")
    heightFeet = input("How many FEET? ")
    heightInches = input("And how many INCHES? ")

# Conversion STR -> INT
heightFeet = int(heightFeet)
heightInches = int(heightInches)

# Computing the HEIGHT (centimeters)
heighCentimeters = (heightInches * 2.54 + heightFeet * 12 * 2.54)

# Displaying the RESULT
print("YOUR HEIGHT is %.2f" % heighCentimeters + " Centimeters")
