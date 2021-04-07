"""
The program generates and displays a DECKS of 52 PLAYING CARDS 
(each card represented using two chars).
After that, it displays the same DECK of CARDS, 
SHUFFLED using an UNBIASED ALGORITHM.
"""

# IMPORT RANDOM module
import random


# START Definition of the FUNCTIONS

def createDeck():
    deck_cards = []
    suits_cards = ["s", "h", "d", "c"]
    faces_cards = ["A", "T", "J", "Q", "K"]
    for suit in range(1, 5):     # from 1 to 4
        for value in range(1, 14):   # from 1 to 13
            card = ""
            if value == 1:
                card += faces_cards[value-1]
            elif 2 <= value <= 9:
                card += str(value)
            else:
                card += faces_cards[value-9]
            card += suits_cards[suit-1]
            deck_cards.append(card)
    return deck_cards


# possible evolution -> Python's built-in shuffle function
def shuffleDeckCards(deck_cards):
    # Copy of the original deck of cards
    deck_cards_shuffled = deck_cards[:]
    number_cards = len(deck_cards_shuffled)
    for i_origin in range(number_cards):
        card_tmp = deck_cards_shuffled[i_origin]
        # Index -> from i_origin to 51
        i_destination = random.randint(i_origin, number_cards-1)
        deck_cards_shuffled[i_origin] = deck_cards_shuffled[i_destination]
        deck_cards_shuffled[i_destination] = card_tmp
    return deck_cards_shuffled


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Generation of the DECKS of CARDS
    deck_cards = createDeck()
    deck_cards_shuffled = shuffleDeckCards(deck_cards)

    # Displaying the DECKS of the CARDScls
    print("ORIGINAL DECK -> ", end="")
    for card in deck_cards:
        print(card, end=" ")
    print("({} cards)".format(len(deck_cards)))
    print("DECK SHUFFLED -> ", end="")
    for card in deck_cards_shuffled:
        print(card, end=" ")
    print("({} cards)".format(len(deck_cards_shuffled)))


if __name__ == "__main__":
    main()
