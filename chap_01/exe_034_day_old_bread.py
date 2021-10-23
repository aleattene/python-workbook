"""
A bakery sells loaves of bread for €3.49 each.
Day old bread is discounted by 60 percent.
Write a program that begins by reading
the number of loaves of day old bread being purchased from the user.
Then your program should display:
- the regular price for the bread,
- the discount because it is a day old, and
- the total price.
Each of these amounts should be displayed on its own line with an appropriate label.
All of the values should be displayed using two decimal places, and
the decimal points in all of the numbers should be aligned
when reasonable values are entered by the user.
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


# Conversion STR -> INT
loavesBreadDO = int(loavesBreadDO)


# COST Computing
costLB = costLoavesBread(loavesBreadDO)
discount = discount(costLB, 0.6)
costFinal = costLB - discount


# Displaying the RESULTS (float formatted with two decimal digits after comma)
print("COST LOAVES BREAD = $ %5.2f" % costLB)
print("   DISCOUNT D.O.B = $ %5.2f" % discount)
print("            TOTAL = $ %5.2f" % costFinal)
