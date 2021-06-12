# My own messing about first
from random import shuffle
list_of_52 = [i + 1 for i in range(0, 52)]

# print(list_of_52)

# shuffle(list_of_52)

# print(list_of_52)


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck():

    def __init__(self):
        self.cards = [Card(s, v) for v in ("A", "2", "3", "4", "5", "6", "7", "8", "9",
                                           "10", "J", "Q", "K") for s in ("Hearts", "Diamonds", "Clubs", "Spades")]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        # return shuffle(self.cards)
        shuffle(self.cards)
        return self # Colt's version - convention to return self

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        num = min(num, self.count())
        # if num == 1:
        #     return self.cards.pop()
        res = self.cards[-num:]
        del self.cards[-num:]
        return res

    def deal_card(self):
        # return self._deal(1)
        return self._deal(1)[0] # Colt's solution - better, because avoids pop()

    def deal_hand(self, num):
        return self._deal(num)


# test_deck = [Card(s, v) for v in values for s in suits]


deck = Deck()
deck.shuffle()
# print(deck.cards[-5:])
hand = deck.deal_hand(50)
card = deck.deal_card()


print(hand)
print(card)
print(deck.count())
hand2 = deck.deal_hand(2)
print(hand2)
