'''
Standard 52-card poker deck
'''

from math import floor
from random import shuffle


class Card:
    RANK_FACTOR = 13
    SUIT_FACTOR = 4

    def __init__(self, code):
        if code < 0 or code > 51:
            raise ValueError("Card.__init__: Invalid code ({})".format(code))
        self.code = code
        rank = floor(code / 4) % Card.RANK_FACTOR
        if rank == 0:
            self.rank = 'A'
        elif rank == 1:
            self.rank = 'K'
        elif rank == 2:
            self.rank = 'Q'
        elif rank == 3:
            self.rank = 'J'
        elif rank == 4:
            self.rank = 'T'
        elif rank == 5:
            self.rank = '9'
        elif rank == 6:
            self.rank = '8'
        elif rank == 7:
            self.rank = '7'
        elif rank == 8:
            self.rank = '6'
        elif rank == 9:
            self.rank = '5'
        elif rank == 10:
            self.rank = '4'
        elif rank == 11:
            self.rank = '3'
        else:
            self.rank = '2'
        suit = self.code % Card.SUIT_FACTOR
        if suit == 0:
            self.suit = 's'
        elif suit == 1:
            self.suit = 'h'
        elif suit == 2:
            self.suit = 'd'
        else:
            self.suit = 'c'

    def __str__(self):
        return self.rank + self.suit


class Deck:

    CARD_CNT = 52

    def __init__(self):
        self.cur = 0
        self.cards = [Card(j) for j in range(0, Deck.CARD_CNT)]

    def shuffle_deck(self):
        self.cur = 0
        shuffle(self.cards)

    def next_card(self):
        if self.cur == Deck.CARD_CNT:
            raise IndexError("Deck.next_card: No more cards in deck")
        card = self.cards[self.cur]
        self.cur += 1
        return card




