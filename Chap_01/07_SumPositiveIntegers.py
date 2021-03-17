"""
Program that receives from the USER a POSITIVE INTEGER "n"
and then DISPLAYS the SUM of positive integers "from 1 to n".
"""

# Acquisition of DATA entered by the USER
n = int(input("Enter the NUMBER POSITIVE INTEGER: "))

# Computing the SUM of positive integers "from 1 to n"
somma = (n * (n + 1)) / 2

# Displaying the RESULT 
print("The SUM of the numbers from 1 to %i" % n + " is equal to %i" % somma)
