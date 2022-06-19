# @author Jungjae Lee
# Independent Project
# Created on June 18, 2022
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
# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# --------------------------------------------------------------------------------
# ------------------------------------- Cards ------------------------------------
def blackjack_game(deck):
    player_cards = []
    dealer_cards = []

    # Beginning
    player_cards = 0
    dealer_cards = 0

