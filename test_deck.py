import unittest
from deck import Deck
from playing_card import PlayingCard

class TestDeck(unittest.TestCase):
    """Unit tests for the Deck class"""

    def setUp(self):
        """Create a fresh deck before each test"""
        self.deck = Deck()

    def test_deck_initialization(self):
        """Test if a new deck contains 52 unique cards"""
        self.assertEqual(len(self.deck.cards), 52)

        unique_cards = set(str(card) for card in self.deck.cards)
        self.assertEqual(len(unique_cards), 52)  # Ensure no duplicates

    def test_shuffle_changes_order(self):
        """Test if shuffling changes the deck order"""
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_draw_card_reduces_deck_size(self):
        """Test if drawing a card reduces the deck size"""
        initial_size = len(self.deck.cards)
        drawn_card = self.deck.draw()
        
        self.assertIsInstance(drawn_card, PlayingCard)
        self.assertEqual(len(self.deck.cards), initial_size - 1)

    def test_draw_from_empty_deck_raises_error(self):
        """Test if drawing from an empty deck raises a ValueError"""
        for _ in range(52):  # Draw all cards
            self.deck.draw()

        with self.assertRaises(ValueError):
            self.deck.draw()

if __name__ == "__main__":
    unittest.main()
