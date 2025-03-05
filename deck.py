import random
from playing_card import PlayingCard

class Deck:
    """A deck of playing cards"""

    def __init__(self):
        """Initialize a full deck of 52 cards"""
        self.cards = [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck"""
        if not self.cards:
            raise ValueError("The deck is empty!")
        return self.cards.pop()