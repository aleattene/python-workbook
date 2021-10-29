"""
The edit distance between two strings is a measure of their similarity.

The smaller the edit distance, the more similar the strings are with regard to the minimum number of insert,
delete and substitute operations needed to transform one string into the other.
Consider the strings kitten and sitting.

The first string can be transformed into the second string with the following operations: Substitute the k with an s,
substitute the e with an i, and insert a g at the end of the string.
This is the smallest number of operations that can be performed to transform kitten into sitting.

As a result, the edit distance is 3.

Write a recursive function that computes the edit distance between two strings.

Use the following algorithm:

Let s and t be the strings
    If the length of s is 0 then
        Return the length of t
    Else if the length of t is 0 then
        Return the length of s
    Else
        Set cost to 0
    If the last character in s does not equal the last character in t then
        Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one
            in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all
            characters except the last one in t, plus 1
        Set d3 equal to the edit distance between all characters except the last one
            in s, and all characters except the last one in t, plus cost Return the minimum of d1, d2 and d3
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
