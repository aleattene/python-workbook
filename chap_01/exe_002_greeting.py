"""
Program that asks the USER to enter his/her NAME and then 
shows a GREETING MESSAGE (using the name entered by the user).
"""

# Acquisition of DATA entered by the USER
name = input("Please, enter your name: ").capitalize()
surname = input("Please, enter your surname: ").capitalize()

# Display of the GREETING MESSAGE
print(f'Hello {surname} {name}.')
