"""
The program generates a DECKS of 52 PLAYING CARDS 
(each card represented using two chars)
and SHUFFLES it using an UNBIASED ALGORITHM.
After that, it deals out four hands of five-card each.
Finally displays the cards dealt for each player 
and the cards remaining in the deck after the distribution.
"""

# IMPORT RANDOM module
import random


# START Definition of the FUNCTIONS

def createDeck():       # possible evolution -> import module
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


def dealHandsCards(num_heads, num_cards_hand, deck_cards_shuffled):
    hands_cards_dealt = []
    for i in range(num_heads):
        # One list for each hand of cards
        hands_cards_dealt.append([])
    for card in range(num_cards_hand):      # cards -> from 1 to 5 (index from 0 to 4)
        for hand in range(num_heads):       # hands -> from 1 to 4 (index from 0 to 3)
            cards_in_deck = len(deck_cards_shuffled)
            # Index from 0 to 51 (decreasing)
            i_card = random.randint(0, cards_in_deck-1)
            # card[i_card] from deck to player_hand[hand]
            hands_cards_dealt[hand].append(deck_cards_shuffled[i_card])
            # Removing card[i_card] from original deck (shuffled)
            deck_cards_shuffled.pop(i_card)
    return hands_cards_dealt


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Declaration of the VARIABLES / CONSTANTS
    NUM_HEADS = 4
    NUM_CARDS_HEAD = 5

    # Generation of the DECKS of CARDS
    deck_cards = createDeck()
    deck_cards_shuffled = shuffleDeckCards(deck_cards)

    # Generation of the LIST of LISTS (each LIST containing ONE HANDS of CARDS)
    hands_dealt = dealHandsCards(
        NUM_HEADS, NUM_CARDS_HEAD, deck_cards_shuffled)

    # Display of CARD HANDS for EACH PLAYER
    for i_hand in range(len(hands_dealt)):
        print("PLAYER {} -> ".format(i_hand+1), end="")
        for i_card in hands_dealt[i_hand]:
            print(i_card, end=" ")
        print("")

    # Display of the CARDS REMAINING in the DECK after distribution
    print("REMAINING cards in the DECK -> ", end="")
    for card in deck_cards_shuffled:
        print(card, end=" ")
    print("({} cards)".format(len(deck_cards_shuffled)))


if __name__ == "__main__":
    main()
