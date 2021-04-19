"""
The program receives TWO WORDS from the USER 
and return their EDIT DISTANCE, 
considering that the EDIT DISTANCE is 
the MINIMUM NUMBER of INSERT, DELETE and SUBSTITUTE OPERATIONS 
needed to TRANSFORM ONE word into the OTHER.
"""


# START Definition of FUNCTION


def computeEditDistance(word_1, word_2):
    # BASE CASE
    if len(word_1) == 0:
        return len(word_2)
    elif len(word_2) == 0:
        return len(word_1)
    # RECURSIVE CASES
    else:
        cost = 0
        if word_1[-1] != word_2[-1]:
            cost = 1
        d1 = computeEditDistance(word_1[:-1], word_2) + 1
        d2 = computeEditDistance(word_1, word_2[:-1]) + 1
        d3 = computeEditDistance(word_1[:-1], word_2[:-1]) + cost
        return min(d1, d2, d3)


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of the WORDS entered by the USER
    word_1 = input("Enter the FIRST WORD: ")
    word_2 = input("Enter the SECOND WORD: ")

    # EDIT DISTANCE computing
    edit_distance = computeEditDistance(word_1, word_2)

    # Displaying the RESULTS
    print("The EDIT DISTANCE between the words \"{}\" and \"{}\" is ({}).".format(
        word_1, word_2, edit_distance))


if __name__ == "__main__":
    main()
