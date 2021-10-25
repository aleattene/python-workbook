"""
The program displays a TABLE with:
- ORIGINAL PRICE,
- AMOUNT of the DISCOUNT (60% of original price), 
- NEW PRICE after applying the discount,  
for PURCHASES of $4.95, $9.95, $14.95, $19.95 and $24.95.
"""

# PURCHASES list and DISCOUNT percentage
purchases = [4.95, 9.95, 14.95, 19.95, 24.95]
DISCOUNT = 0.6      # discount 60%

# Generation and display of the PURCHASES TABLE
print("************************")
print("        PURCHASES       ")
print("************************")

for i in range(5):
    originalPrice = purchases[i]
    discount = originalPrice * DISCOUNT
    newPrice = originalPrice - discount
    print("ORIGINAL PRICE   $ %5.2f" % originalPrice)
    print("  60" + chr(37) + " discount   $ %5.2f" % discount)
    print("     NEW PRICE   $ %5.2f" % newPrice)
    print("************************")

print("************************")
