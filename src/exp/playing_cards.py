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
        self.numeric_rank = floor(code / 4) % Card.RANK_FACTOR
        if self.numeric_rank == 0:
            self.alphabetic_rank = 'A'
        elif self.numeric_rank == 1:
            self.alphabetic_rank = 'K'
        elif self.numeric_rank == 2:
            self.alphabetic_rank = 'Q'
        elif self.numeric_rank == 3:
            self.alphabetic_rank = 'J'
        elif self.numeric_rank == 4:
            self.alphabetic_rank = 'T'
        elif self.numeric_rank == 5:
            self.alphabetic_rank = '9'
        elif self.numeric_rank == 6:
            self.alphabetic_rank = '8'
        elif self.numeric_rank == 7:
            self.alphabetic_rank = '7'
        elif self.numeric_rank == 8:
            self.alphabetic_rank = '6'
        elif self.numeric_rank == 9:
            self.alphabetic_rank = '5'
        elif self.numeric_rank == 10:
            self.alphabetic_rank = '4'
        elif self.numeric_rank == 11:
            self.alphabetic_rank = '3'
        else:
            self.alphabetic_rank = '2'
        self.numeric_suit = self.code % Card.SUIT_FACTOR
        if self.numeric_suit == 0:
            self.alphabetic_suit = 's'
        elif self.numeric_suit == 1:
            self.alphabetic_suit = 'h'
        elif self.numeric_suit == 2:
            self.alphabetic_suit = 'd'
        else:
            self.alphabetic_suit = 'c'

    def __str__(self):
        return self.alphabetic_rank + self.alphabetic_suit
    
    def getNumRank(self):
        return self.numeric_rank
    
    def getNumSuit(self):
        return self.numeric_suit


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
    
    def reset(self):
        self.cur = 0




