"""
The program requires the USER to CHOOSE a MENU from those displayed and 
RETURNS:
- the grand TOTAL for the MEAL
- the TAX amount (FLAT tax : 15%)
- the TIP amount (18% of the meal without the tax)
"""

# Displaying the MENU
print("MENU 1 - Primo, Secondo, Contorno, Caffè ($ 12.00)")
print("MENU 2 - Primo, Secondo, Contorno, Frutta, Caffè ($ 15.00)")
print("MENU 3 - Primo, Secondo, Contorno, Frutta, Caffè, Dolce ($ 18.00)")
print("MENU 4 - Antipasto, Primo, Secondo, Contorno, Frutta, Caffè, Dolce ($ 21.00)")

# Declaration of VARIABLES / COSTANTS
TAX = 0.15      # Flat tax = 15%
TIP = 0.18      # 18% of the meal without the tax

# DICTIONARY { MENU : PRICE }
prices = {
    "1": 12.00,
    "2": 15.00,
    "3": 18.00,
    "4": 21.00
}

# Acquisition and Control of the DATA entered by the USER
menu = input("Which MENU would you like to order? 1, 2, 3 or 4? ")
while menu not in prices.keys() or menu == "":
    print("MENU not available. Try again.")
    menu = input("Which MENU would you like to order? 1, 2, 3 or 4? ")

# Computing the TOTAL of MEAL (including both the TAX and the TIP)
priceMenu = prices.get(menu)
amountTax = priceMenu * TAX
amountTip = (priceMenu - amountTax) * TIP

# Displaying the RESULTS (Float with two decimal digits after comma)
print("For your ORDER - TOTAL € %.2f" % priceMenu)
print("Included TAX for € %.2f" %
      amountTax + " and TIP for € %.2f " % amountTip)
