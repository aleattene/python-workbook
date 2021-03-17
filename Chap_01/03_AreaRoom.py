
""" 
Program that asks the USER to enter the SIZE of a ROOM 
(width and length) to calculate its AREA. 
The final result is then displayed.
"""
# Acquisition of DATA entered by the USER
width = float(input("Enter the WIDTH of your room (meters): "))
length = float(input("Enter also the LENGTH (meters): "))

# Computing the ROOM AREA (square meters)
area = width * length

# Displaying the ROOM AREA
print("The AREA of your ROOM is " + str(area) + " square meters")
