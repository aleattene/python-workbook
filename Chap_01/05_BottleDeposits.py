"""
The program receives from the USER the NUMBER of DRINK CONTAINERS
and COMPUTES the REFUND in case you recycle them, considering:
-> $ 0.10 for each container of 1 liter or less,
-> $ 0.25 for each container greater than 1 liter. 
"""

# Declaration VARIABLES / COSTANTS
REFUND_UNDER_EQUAL_1L = 0.10       # refund drink container <= 1 liter
REFUND_OVER_1L = 0.25              # refund drink container > 1 liter

# Acquisition USER DATA
drinkContainerUnderEqual1 = int(input(
    "How many DRINK CONTAINERS, holding ONE LITER or LESS , do you have to RECYCLE? "))
drinkContainerOver1 = int(input("And how many, holding MORE THAN ONE LITER? "))

# Computing REFUND
refund = (REFUND_UNDER_EQUAL_1L * drinkContainerUnderEqual1) + \
    (REFUND_OVER_1L * drinkContainerOver1)

# Displaying REFUND (two decimal digits after the comma)
print("Your REFUND is $ %3.2f" % refund)
