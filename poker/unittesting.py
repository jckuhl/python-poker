import unittest
import cards
import poker


class CardTests(unittest.TestCase):

    def setUp(self):
        self.ace = cards.Card(1, 14)
        self.deuce = cards.Card(3, 2)
        self.deck = poker.FiftyTwoDeck
        self.hand = poker.FiveCardPokerHand

    def test_card_equal_to_card(self):
        self.assertEqual(self.ace, cards.Card(1, 14))

    def test_card_greater(self):
        self.assertGreater(self.ace, self.deuce)

    def test_card_lesser(self):
        self.assertLess(self.deuce, self.ace)


if __name__ == "__main__":
    unittest.main()
