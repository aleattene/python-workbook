
""" 
Write a program that asks the user to enter the width and length of a room.
Once these values have been read, your program should compute and display the area of the room.
The length and the width will be entered as floating-point numbers.
Include units in your prompt and output message; either feet or meters,
depending on which unit you are more comfortable working with.
"""

# Acquisition of DATA entered by the USER
width = float(input("Enter the WIDTH of your room (meters): "))
length = float(input("Enter also the LENGTH (meters): "))

# Computing the ROOM AREA (square meters)
area = width * length

# Displaying the ROOM AREA
print(f'The AREA of your ROOM is {area} square meters.')
