"""
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00.
Admission for all other guests is $23.00.
Create a program that
begins by reading the ages of all of the guests in a group from the user,
with one age entered on each line.
The user will enter a blank line to indicate that there are no more guests in the group.
Then your program should display the admission cost for the group with an appropriate message.
The cost should be displayed using two decimal places.
"""

# START Definition of FUNCTION


def valutaEntry(numero):
    if numero.isdigit():
        if 0 < int(numero) <= 120:
            return True
    return False


def computesAdmissionPrice(age):
    age = int(age)
    if age <= 2:
        admissionPrice = 0              # no charge
    elif 3 <= age <= 14:
        admissionPrice = 14.00          # $14.00
    elif 15 <= age <= 64:
        admissionPrice = 23.00          # $23.00
    else:   # equal and over 65 years
        admissionPrice = 18.00          # $18.00
    return admissionPrice


# END Definition of FUNCTION


# Declaration of VARIABLES
groupCost = 0


# Acquisition and Control of the DATA entered by the USER
age = input("Enter the AGE of the GUEST: ")
ageValidated = valutaEntry(age)

while not(ageValidated):
    print("Incorrect entry. Try again.")
    age = input("Enter the AGE of the GUEST: ")
    ageValidated = valutaEntry(age)

while age != "":
    if ageValidated:
        admissionPrice = computesAdmissionPrice(age)    # ADMISSION PRICE computing
        groupCost += admissionPrice                     # ADMISSION PRICE for the GROUP
        age = input("Enter the AGE of the GUEST (or EMPTY line to QUIT): ")
        ageValidated = valutaEntry(age)
    else:
        print("Incorrect entry. Try again.")
        age = input("Enter the AGE of the GUEST (or EMPTY line to QUIT): ")
        ageValidated = valutaEntry(age)


# Displaying the RESULT
print("The TOTAL ADMISSION PRICE to the ZOO for the GROUP is $ %.2f" % groupCost)
