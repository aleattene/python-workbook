"""
The program receives from the USER an INTEGER number from 1 to 12
and displays the song TWELVE DAYS OF CHRISTMAS
up to the VERSE corresponding to the NUMBER INSERTED.
"""

# START Definition of the FUNCTIONS


def valutaEntry(number):            # Possible evolution -> IMPORT module
    # Check Entry -> INT POSITIVE
    return True


def integerToOrdinal(number):       # Possible evolution -> IMPORT module
    ordinal_numbers = {
        "1": "FIRST",
        "2": "SECOND",
        "3": "THIRD",
        "4": "FOURTH",
        "5": "FIFTH",
        "6": "SIXTH",
        "7": "SEVENTH",
        "8": "EIGHTH",
        "9": "NINTH",
        "10": "TENTH",
        "11": "ELEVENTH",
        "12": "TWELFTH"
    }
    if number in ordinal_numbers.keys():
        return ordinal_numbers[number]
    else:
        return "OUT of RANGE"


def displayVerse(verse_number):
    print("On the {} day of Christmas my true love sent to me:".format(
        integerToOrdinal(verse_number).lower()))
    verse_number = int(verse_number)
    if verse_number == 12:
        print("Twelve drummers drumming,")
    if verse_number >= 11:
        print("Eleven pipers piping,")
    if verse_number >= 10:
        print("Ten lords a-leaping,")
    if verse_number >= 9:
        print("Nine ladies dancing,")
    if verse_number >= 8:
        print("Eight maids a-milking,")
    if verse_number >= 7:
        print("Seven swans a-swimming,")
    if verse_number >= 6:
        print("Six geese a-laying,")
    if verse_number >= 5:
        print("Five gold rings,")
    if verse_number >= 4:
        print("Four calling birds,")
    if verse_number >= 3:
        print("Three French hens,")
    if verse_number >= 2:
        print("Two turtle doves,")
    if verse_number > 1:
        print("And a partridge in a pear tree.")
    elif verse_number == 1:
        print("A partridge in a pear tree.")


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    verse_number = input("Enter the NUMBER of the VERSE (from 1 to 12): ")

    # Displaying the RESULTS
    displayVerse(verse_number)


if __name__ == "__main__":
    main()
