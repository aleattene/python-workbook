"""
The program receives from the USER
the NUMBER of ITEMS PURCHASED
and returns (displaying it) the SHIPPING CHARGE,
considering that:
- rate for the first item = $10.95
- rate for each subsequent item = $2.95
"""


# START Definition of FUNCTIONS


def valutaEntry(number):
    # Check Entry -> INT POSITIVE
    return True


def shippingCharge(items):
    FIRST_ITEM = 10.95                    # RATE FIRST ITEM = $10.95
    SUBSEQUENT_ITEM = 2.95                # RATE EACH SUBSEQUENT ITEM = $2.95
    shipping_charge = FIRST_ITEM + (SUBSEQUENT_ITEM * (items - 1))
    return shipping_charge


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
items = input("Enter the NUMBER of ITEMS PURCHASED: ")
items_validated = valutaEntry(items)

while not(items_validated):
    print("Incorrect entry. Try again.")
    items = input("Enter the NUMBER of ITEMS PURCHASED: ")
    items_validated = valutaEntry(items)


# ITEMS PURCHASED conversion : STR -> INT
items = int(items)


# SHIPPING CHARGE computing
shipping_charge = shippingCharge(items)


# Displaying the RESULT
print("The SHIPPING CHARGE for this PURCHASE (n. " + str(items) +
      " items) is $ %.2f" % shipping_charge + ".")
