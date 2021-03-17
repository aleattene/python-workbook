
""" 
Program that asks the USER to enter the SIZE of a ROOM 
(width and length) to calculate its AREA. 
The final result is then displayed.
"""

# Acquisition USER DATA
width = float(input("Enter the WIDTH of your room (meters): "))
length = float(input("Enter also the LENGTH (meters): "))

# Calculation ROOM AREA (square meters)
area = width * length

# Displaying FINAL RESULT
print("The AREA of your ROOM is " + str(area) + " square meters")
