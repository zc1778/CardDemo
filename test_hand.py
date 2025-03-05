import unittest
from hand import Hand
from playing_card import PlayingCard

class TestHand(unittest.TestCase):
    """Unit tests for the Hand class"""

    def setUp(self):
        """Create a fresh hand before each test"""
        self.hand = Hand()
        self.card1 = PlayingCard("A", "Spades")
        self.card2 = PlayingCard("10", "Hearts")

    def test_add_card(self):
        """Test adding cards to the hand"""
        self.hand.add_card(self.card1)
        self.assertIn(self.card1, self.hand.cards)
        self.assertEqual(self.hand.count(), 1)

    def test_display_empty_hand(self):
        """Test displaying an empty hand"""
        self.assertEqual(self.hand.display(), "The hand is empty.")

    def test_display_hand_with_cards(self):
        """Test displaying a hand with cards"""
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.display(), "A of Spades, 10 of Hearts")

    def test_count_cards(self):
        """Test counting the number of cards in the hand"""
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.count(), 2)

    def test_add_invalid_card(self):
        """Test adding an invalid card raises a ValueError"""
        with self.assertRaises(ValueError):
            self.hand.add_card("Not a card")  # Passing a string instead of a PlayingCard

if __name__ == "__main__":
    unittest.main()
