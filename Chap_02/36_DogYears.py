"""
The Program receives from the USER a HUMAN AGE 
and transforms it into the CANINE AGE, considering that:
- the FIRST TWO HUMAN YEARS are equivalent to 10.5 CANINE YEARS
- the FOLLOWING HUMAN YEARS are equivalent to FOUR CANINE YEARS.
"""

# START Definition of FUNCTIONS


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def yearsHumanDog(etaHuman):
    if etaHuman == 1:
        etaDog = 10.5
        return etaDog
    elif etaHuman == 2:
        etaDog = 21
        return etaDog
    else:
        etaDog = 21 + ((etaHuman-2) * 4)
        return etaDog


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
etaHuman = input("Enter the HUMAN Years: ")
etaHumanIntPositive = valutaIntPositive(etaHuman)

while not(etaHumanIntPositive):
    print("Incorrect entry. Try again.")
    etaHuman = input("Enter the HUMAN Years: ")
    etaHumanIntPositive = valutaIntPositive(etaHuman)


# Conversion STR -> INT
etaHuman = int(etaHuman)


# DOG YEARS computing
etaDog = yearsHumanDog(etaHuman)


# Displaying the RESULTS
if etaHuman == 1:
    print(str(etaHuman) + " HUMAN year is equal to " + str(etaDog) + " DOG years.")
else:
    print(str(etaHuman) + " HUMAN years is equal to " + str(etaDog) + " DOG years.")
