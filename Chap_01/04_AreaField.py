
""" 
Program that asks the USER to enter the SIZE of a FARMER'S FIELD 
(width and length) to calculate its AREA in ACRES (1 ACRE = 43.560 square feet). 
The final result is then displayed.
"""

# Acquisition USER DATA
width = float(input("Enter the WIDTH of a FARMER'S FIELD (feet): "))
length = float(input("Enter also the LENGTH (feet): "))

# Computing FARMER'S FIELD (acres) -> (1 ACRE = 43.560 square feet)
area = (width * length) / 43560

# Displaying FINAL RESULT (Formatting AREA value with 3 decimal places after comma)
print("The AREA of a farmer's field is " + "%.3f" % area + " acres")
