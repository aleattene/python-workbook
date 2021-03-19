"""
The Program receives from the USER a YEAR
and in according to the CHINESE ZODIAC, 
returns (displaying it) the corresponding ANIMAL.
"""

# START Definition of FUNCTIONS


def valutaInt(numero):
    if numero.isdigit():
        return True
    return False


def yearToAnimal(year):
    if year % 12 == 8:
        return "DRAGON"
    elif year % 12 == 9:
        return "SNAKE"
    elif year % 12 == 10:
        return "HORSE"
    elif year % 12 == 11:
        return "SHEEP"
    elif year % 12 == 0:
        return "MONKEY"
    elif year % 12 == 1:
        return "ROOSTER"
    elif year % 12 == 2:
        return "DOG"
    elif year % 12 == 3:
        return "PIG"
    elif year % 12 == 4:
        return "RAT"
    elif year % 12 == 5:
        return "OX"
    elif year % 12 == 6:
        return "TIGER"
    elif year % 12 == 7:
        return "HARE"


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
year = input(
    "Enter the YEAR for which you want to know the ANIMAL assigned by the CHINESE ZODIAC: ")
yearValidated = valutaInt(year)

while not(yearValidated):
    print("Incorrect entry. Try again.")
    year = input(
        "Enter the YEAR for which you want to know the ANIMAL assigned by the CHINESE ZODIAC: ")
    yearValidated = valutaInt(year)


# Conversion STR -> INT
year = int(year)


# Evaluation YEAR -> ANIMAL of the CHINESE ZODIAC
animal = yearToAnimal(year)


# Displaying the RESULTS
print("In the CHINESE ZODIAC " + str(year) +
      " is the YEAR of the " + animal + ".")
