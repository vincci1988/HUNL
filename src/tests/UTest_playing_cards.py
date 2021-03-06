import unittest
from src.exp.playing_cards import Deck


class PlayingCardTests(unittest.TestCase):

    def testDeck(self):
        deck = Deck()
        self.assertEqual("As", str(deck.next_card()))
        self.assertEqual("Ah", str(deck.next_card()))
        self.assertEqual("Ad", str(deck.next_card()))
        self.assertEqual("Ac", str(deck.next_card()))
        self.assertEqual("Ks", str(deck.next_card()))
        self.assertEqual("Kh", str(deck.next_card()))
        self.assertEqual("Kd", str(deck.next_card()))
        self.assertEqual("Kc", str(deck.next_card()))
        self.assertEqual("Qs", str(deck.next_card()))
        self.assertEqual("Qh", str(deck.next_card()))
        self.assertEqual("Qd", str(deck.next_card()))
        self.assertEqual("Qc", str(deck.next_card()))
        self.assertEqual("Js", str(deck.next_card()))
        self.assertEqual("Jh", str(deck.next_card()))
        self.assertEqual("Jd", str(deck.next_card()))
        self.assertEqual("Jc", str(deck.next_card()))
        self.assertEqual("Ts", str(deck.next_card()))
        self.assertEqual("Th", str(deck.next_card()))
        self.assertEqual("Td", str(deck.next_card()))
        self.assertEqual("Tc", str(deck.next_card()))
        self.assertEqual("9s", str(deck.next_card()))
        self.assertEqual("9h", str(deck.next_card()))
        self.assertEqual("9d", str(deck.next_card()))
        self.assertEqual("9c", str(deck.next_card()))
        self.assertEqual("8s", str(deck.next_card()))
        self.assertEqual("8h", str(deck.next_card()))
        self.assertEqual("8d", str(deck.next_card()))
        self.assertEqual("8c", str(deck.next_card()))
        self.assertEqual("7s", str(deck.next_card()))
        self.assertEqual("7h", str(deck.next_card()))
        self.assertEqual("7d", str(deck.next_card()))
        self.assertEqual("7c", str(deck.next_card()))
        self.assertEqual("6s", str(deck.next_card()))
        self.assertEqual("6h", str(deck.next_card()))
        self.assertEqual("6d", str(deck.next_card()))
        self.assertEqual("6c", str(deck.next_card()))
        self.assertEqual("5s", str(deck.next_card()))
        self.assertEqual("5h", str(deck.next_card()))
        self.assertEqual("5d", str(deck.next_card()))
        self.assertEqual("5c", str(deck.next_card()))
        self.assertEqual("4s", str(deck.next_card()))
        self.assertEqual("4h", str(deck.next_card()))
        self.assertEqual("4d", str(deck.next_card()))
        self.assertEqual("4c", str(deck.next_card()))
        self.assertEqual("3s", str(deck.next_card()))
        self.assertEqual("3h", str(deck.next_card()))
        self.assertEqual("3d", str(deck.next_card()))
        self.assertEqual("3c", str(deck.next_card()))
        self.assertEqual("2s", str(deck.next_card()))
        self.assertEqual("2h", str(deck.next_card()))
        self.assertEqual("2d", str(deck.next_card()))
        self.assertEqual("2c", str(deck.next_card()))
        try:
            deck.next_card()
        except IndexError:
            self.assertTrue(True)
        else:
            self.assertFalse(msg = "Failed to raise IndexError Exception")
        finally:
            deck.shuffle_deck()
            print("Shuffled deck: ", end = "")
            for _ in range(0, Deck.CARD_CNT):
                print(deck.next_card(), end = "")
            print()
