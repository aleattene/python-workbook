"""
In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them.
In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit,
and drink containers holding more than one liter have a $0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund
that will be received for returning those containers.
Format the output so that it includes a dollar sign and two digits to the right of the decimal point.
Remember:
-> $ 0.10 for each container of 1 liter or less,
-> $ 0.25 for each container greater than 1 liter. 
"""

# Declaration of VARIABLES / COSTANTS
REFUND_UNDER_EQUAL_1L = 0.10       # refund drink container <= 1 liter
REFUND_OVER_1L = 0.25              # refund drink container > 1 liter

# Acquisition of DATA entered by the USER
drinkContainerUnderEqual1 = int(input(
    "How many DRINK CONTAINERS, holding ONE LITER or LESS , do you have to RECYCLE? "))
drinkContainerOver1 = int(input("And how many, holding MORE THAN ONE LITER? "))

# Computing the REFUND
refund = (REFUND_UNDER_EQUAL_1L * drinkContainerUnderEqual1) + \
    (REFUND_OVER_1L * drinkContainerOver1)

# Displaying the REFUND (two decimal digits after the comma)
print("Your REFUND is $ %3.2f" % refund)
