"""
The Program receives from the USER a MEASURE in FEET
and converts it to INCHES, YARDS and MILES.
"""

# Acquisition and Control of the DATA entered by the USER
distanceFeet = input("Enter the measurement (FEET): ")

while not(distanceFeet.isdigit() and distanceFeet != "0"):
    print("Incorrect entry. Try again.")
    distanceFeet = input("Enter the measurement (FEET): ")

# Conversion STR -> INT
distanceFeet = int(distanceFeet)

# Computing of the MEASURE (in INCHES, YARDS and MILES)
distanceInches = distanceFeet * 12
distanceYards = distanceFeet / 3
distanceMiles = distanceYards / 1760

# Displaying the RESULTS
print("The DISTANCE %i" % distanceFeet + " FEET is equal to:")
print("- %i" % distanceInches + " inches")
print("- %.2f" % distanceYards + " yards")
print("- %.3f" % distanceMiles + " miles")
