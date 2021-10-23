"""
The Program receives from the USER the NUMBER of LOAVES of DAY OLD BREAD
and calculates the PURCHASE COST, considering that:
- LOAVE of BREAD cost = $ 3.49
- Discount LOAVE of DAY OLD BREAD = 60%
After that, the program displays the RECEIPT with:
- TOTAL COST of LOAVES of BREAD
- DISCOUNT Applied
- TOTAL PURCHASE COST
"""

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def costLoavesBread(loavesBread):
    costLB = loavesBread * 3.49
    return costLB


def discount(cost, percDiscount):
    discount = cost * percDiscount
    return discount


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
loavesBreadDO = input("Enter the NUMBER of DAY OLD LOAVES of BREAD: ")
loavesBreadDOValidated = valutaIntPositive(loavesBreadDO)

while not(loavesBreadDOValidated):
    print("Incorrect entry. Try again.")
    loavesBreadDO = input("Enter the NUMBER of DAY OLD LOAVES of BREAD: ")
    loavesBreadDOValidated = valutaIntPositive(loavesBreadDO)


# Connversion STR -> INT
loavesBreadDO = int(loavesBreadDO)


# COST Computing
costLB = costLoavesBread(loavesBreadDO)
discount = discount(costLB, 0.6)
costFinal = costLB - discount


# Displaying the RESULTS (float formatted with two decimal digits after comma)
print("COST LOAVES BREAD = $ %5.2f" % costLB)
print("   DISCOUNT D.O.B = $ %5.2f" % discount)
print("            TOTAL = $ %5.2f" % costFinal)
