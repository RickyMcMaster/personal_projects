from deck_of_cards import Card, Deck
import unittest
from dad_jokes import joke_finder
# import functions

# new_card = Card("Hearts", "7")
# print(new_card)


class CardTests(unittest.TestCase):
    def card_repr_test(self):
        self.assertEqual(Card("Hearts", "7"), "7 of Hearts")
        self.assertEqual(Card("Clubs", "7"), "7 of Clubs")


if __name__ == "__main__":
    unittest.main()
