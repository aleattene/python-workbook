"""
A particular cell phone plan includes
50 minutes of air time and 50 text messages for € 15.00 a month.
Each additional minute of air time costs € 0.25,
while additional text messages cost € 0.15 each.
All cell phone bills include an additional charge of € 0.44 to support 911 call centers,
and the entire bill (including the 911 charge) is subject to 5 percent sales tax.
Write a program that reads the number of minutes
and text messages used in a month from the user.
Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount.
Only display the additional minute and text message charges
if the user incurred costs in these categories.
Ensure that all of the charges are displayed using 2 decimal places.
Summarizing:
- base charge (included 50 minutes of air time and 50 text messages) = $ 15.00 for month
- each additional minute of air time = $ 0.25
- each additional text messages = $ 0.15
- additional charge to support 911 call centers = $ 0.44
- sales tax = 5 %
"""

# Declaration of VARIABLES / CONSTANTS
BASE_CHARGE = 15.00     # includes 50 minutes of air time and 50 text messages
SERVICE_911CC = 0.44    # additional charge to support 911 call centers


# START Definition of FUNCTIONS


def costMinutes(minutes):
    if minutes <= 50:
        cost = 0
    else:
        cost = (minutes - 50) * 0.25
    return cost


def costTextMessages(numMsg):
    if numMsg <= 50:
        cost = 0
    else:
        cost = (numMsg - 50) * 0.15
    return cost


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter the NUMBER of MINUTES of air time and the TEXT MESSAGES used this MONTH.")
minutes = input("MINUTES: ")
textMsg = input("TEXT MESSAGES: ")

while not(minutes.isdigit() and textMsg.isdigit()):
    print("Incorrect entry. Try again.")
    print("Enter the NUMBER of MINUTES of air time and the TEXT MESSAGES used this MONTH.")
    minutes = input("MINUTES: ")
    textMsg = input("TEXT MESSAGES: ")


# Conversion STR -> INT
minutes = int(minutes)
textMsg = int(textMsg)


# BILL Computing
costMinutes = costMinutes(minutes)
costTextMessages = costTextMessages(textMsg)
billPartial = BASE_CHARGE + costMinutes + costTextMessages + SERVICE_911CC
salesTax = billPartial * 0.05
billTotal = billPartial + salesTax


# Displaying the RESULTS (formatted with total six spaces and two decimal digits after comma)
print("**************** MONTLY BILL ****************")
print("- Base Charge                        $ %6.2f" % BASE_CHARGE)
if costMinutes != 0:
    print("- Additional Minutes Charge          $ %6.2f" % costMinutes)
if costTextMessages != 0:
    print("- Additional TexT Messages Charge    $ %6.2f" % costTextMessages)
print("- 911 Call Center Fee                $ %6.2f" % SERVICE_911CC)
print("- Sales Tax                          $ %6.2f" % salesTax)
print("************************* TOTAL BILL $ %6.2f" % billTotal)
