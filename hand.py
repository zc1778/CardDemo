from playing_card import PlayingCard

class Hand:
    """A class representing a hand of playing cards"""

    def __init__(self):
        """Initialize an empty hand"""
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand"""
        if not isinstance(card, PlayingCard):
            raise ValueError("Only PlayingCard instances can be added to the hand")
        self.cards.append(card)

    def display(self):
        """Display the hand"""
        if not self.cards:
            return "The hand is empty."
        return ", ".join(str(card) for card in self.cards)

    def count(self):
        """Return the number of cards in the hand"""
        return len(self.cards)