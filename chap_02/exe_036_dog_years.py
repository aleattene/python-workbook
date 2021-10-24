"""
It is commonly said that one human year is equivalent to 7 dog years.
However this simple conversion fails
to recognize that dogs reach adulthood in approximately two years.
As a result, some people believe that it is better
to count each of the first two human years as 10.5 dog years,
and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph.
Ensure that your program works correctly
for conversions of less than two human years and
for conversions of two or more human years.
Your program should display an appropriate error message if the user enters a negative number.
Remember that:
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
