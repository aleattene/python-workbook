"""
The program SUMS all of the NUMBERS entered by the USER,
while ignoring any input that is not a VALID NUMBER.
"""

# Import MATH module
import math

# Acquisition and Control of the DATA entered by the USER
number = input("Enter the NUMBER to add: ")

numbers = []
while number != "":
    try:
        # Storing the entered number
        if "." not in number:
            numbers.append(int(number))
        else:
            numbers.append(float(number))
        # Displaying the CURRENT SUM
        current_sum = sum(numbers)
        if current_sum - math.trunc(current_sum) == 0:
            current_sum = int(current_sum)
        print("Current Sum = " + str(current_sum))
        number = input("Enter the NUMBER to add: ")
    # Exception -> Value Error
    except ValueError:
        print("Warning, a NON-NUMERIC value has been entered.")
        number = input("Enter the NUMBER to add: ")

# Displaying the RESULTS
print("The SUM of the NUMBERS entered is {} ".format(current_sum))
print("NUMBERS entered -> ", end="")
if len(numbers) == 0:
    print("NO ONE")
else:
    for value in numbers:
        print(value, end="  ")
