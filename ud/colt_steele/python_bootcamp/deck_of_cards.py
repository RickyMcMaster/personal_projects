from random import shuffle


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
        return self  # Colt's version - convention to return self

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
        # Colt's solution - better, because avoids pop()
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


if __name__ == "__main__":
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
