from deck_of_cards import Card, Deck
import unittest


class CardTests(unittest.TestCase):
    # new_card = 
    def setUp(self):
        self.card = Card("Hearts", "7")
    # print(new_card)

    def card_repr_test(self):
        self.assertEqual(repr(self.card), "7 of Hearts")
        # self.assertEqual(Card("Clubs", "7"), "7 of Clubs")

class DeckTests(unittest.TestCase):
    new_deck = Deck()
    def orig_count(self):
        self.assertEqual(new_deck.count(), 52)

if __name__ == '__main__':
    unittest.main()
