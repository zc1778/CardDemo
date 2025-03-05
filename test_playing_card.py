import unittest

from playing_card import PlayingCard

class TestPlayingCard(unittest.TestCase):

    def test_valid_card(self):
        card = PlayingCard("A", "Hearts")
        self.assertEqual(str(card), "A of Hearts")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            PlayingCard("1", "Hearts")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard("A", "Stars")

    def test_card_equality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("10", "Diamonds")
        self.assertEqual(card1, card2)

    def test_card_inequality(self):
        card1 = PlayingCard("10", "Diamonds")
        card2 = PlayingCard("J", "Diamonds")
        self.assertNotEqual(card1, card2)

if __name__ == "__main__":
    unittest.main()