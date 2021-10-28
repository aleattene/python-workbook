"""
In the game of Scrabble, each letter has points associated with it.
The total score of a word is the sum of the scores of its letters.

More common letters are worth fewer points while less common letters are worth more points.
The points associated with each letter are shown below:

    Points      	            Letters
      1	                A, E, I, L, N, O, R, S, T, U
2	D, G
3	B, C, M, P
4	F, H, V, W, Y
5	K
8	J, X
10	Q, Z
Write a program that computes and displays the Scrabble score for a word.

Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.

Documentation
"""


# START Definition of the FUNCTION


def computeScrabbleScore(word):
    # Dictionary of the scores
    scores_dict = {
        1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    # SCORE counter
    scores = 0
    # Analysis of EACH character of the WORD
    for char in word.upper():
        # Analysis of each KEY within the DICTIONARY
        for k in scores_dict:
            # Evaluation -> char in [chars]
            if char in scores_dict[k]:
                # score INCREASE
                scores += k
    return scores


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    word = input("Enter the WORD for the SCRABBLE game: ")

    # SCORE computing
    scrabble_score = computeScrabbleScore(word)

    # SCORE DISPLAY
    print("The SCRABBLE SCORE for the word \"{}\" is {} points.".format(
        word, scrabble_score))


if __name__ == "__main__":
    main()
