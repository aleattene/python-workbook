
""" 
Program that asks the USER to enter the SIZE of a FARMER'S FIELD 
(width and length) to calculate its AREA in ACRES (1 ACRE = 43.560 square feet). 
The final result is then displayed.
"""

# Acquisition USER DATA
width = float(input("Enter the WIDTH of a FARMER'S FIELD (feet): "))
length = float(input("Enter also the LENGTH (feet): "))

# Computing the FARMER'S FIELD AREA (in acres) -> (1 ACRE = 43.560 square feet)
area = (width * length) / 43560

# Displaying the FARMER'S FIELD AREA (three digital digits after the comma)
print("The AREA of a farmer's field is " + "%.3f" % area + " acres")
