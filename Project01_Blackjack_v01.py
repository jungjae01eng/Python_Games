# @author Jungjae Lee
# Independent Project
# Created on June 18, 2022
# Last Updated on June 19, 2022
# Sources: (1) Create our own Blackjack Game using Python on AskPython
#          (2) __init__ in Python on GeeksforGeeks
#          (3) Unicode Character on FileFormatInfo
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# ----------------------------- Blackjack Game Rules -----------------------------
#   1. The "magic number" for Blackjack is 21.
#   2. If the sum exceeds 21, the player busts and loses instantly.
#   3. If the player gets an exact 21, the player wins.
#   4. Otherwise, the sum of the player's cards must be more than the sum of the dealer's cards.
#   5. Ace can be counted as either 1 or 11 suitable to the player's chances of winning.
#   6. Generally, a dealer needs to keep hitting more cards if the sum of the dealer's cards is less than 17.


# --------------------------------------------------------------------------------
# ------------------------------------- Types ------------------------------------
# * Used the sources (1) and (3) on this section
# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The suit value
suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The card value
cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
               "K": 10}


# --------------------------------------------------------------------------------
# ------------------------------------- Cards ------------------------------------
# We want to print: __________
#                  | A        |
#                  |          |
#                  |     S    |
#                  |          |
#                  |        A |
#                  |__________|


def print_cards(cards):
    s = ""
    for card in cards:
        s = s + "\t __________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t| {}        |".format(card.value)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|          |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|    {}    |".format(card.suit)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|          |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|        {} |".format(card.value)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|__________|"
    print(s)


# --------------------------------------------------------------------------------
deck = []   # There are nothing on the deck
for suit in suits:
    for card in cards:
        deck.append(Card(suits_values[suit], card, cards_values[card]))


# --------------------------------------------------------------------------------
def blackjack_game(deck):
    player_cards = []
    dealer_cards = []

    # Beginning
    player_cards = 0
    dealer_cards = 0

