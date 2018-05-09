
import unittest
from src.exp.holdem_judges import find_best_hand
from src.exp.holdem_judges import compare
from src.exp.holdem_judges import Hand
from src.exp.playing_cards import Card
from math import floor


class HoldemJudgeTest(unittest.TestCase):


    def test_straight_flush(self):
        case = "AdKdQdQcJdTsTd"
        self.assertEqual("Straight Flush: AdKdQdJdTd", str(find_best_hand(str2cards(case))))
        case = "Ad5s5h5d4d3d2d"
        self.assertEqual("Straight Flush: 5d4d3d2dAd", str(find_best_hand(str2cards(case))))
        case = "6s5s5h4s4d3s2s"
        self.assertEqual("Straight Flush: 6s5s4s3s2s", str(find_best_hand(str2cards(case))))
        
        
    def test_four_of_a_kind(self):
        case = "AdTsThTdTc5d2d"
        self.assertEqual("Four of a Kind: TsThTdTcAd", str(find_best_hand(str2cards(case))))
        case = "KsTsJsKcQsKdKh"
        self.assertEqual("Four of a Kind: KsKhKdKcQs", str(find_best_hand(str2cards(case))))
        
        
    def test_full_house(self):
        case = "KsQdJsQcQsKdKh"
        self.assertEqual("Full House: KsKhKdQsQd", str(find_best_hand(str2cards(case))))
        case = "KsAdThAcTsKdKh"
        self.assertEqual("Full House: KsKhKdAdAc", str(find_best_hand(str2cards(case))))
        case = "TsAdThAcTdKd7h"
        self.assertEqual("Full House: TsThTdAdAc", str(find_best_hand(str2cards(case))))
        case = "2sAd2h7c2dKd7h"
        self.assertEqual("Full House: 2s2h2d7h7c", str(find_best_hand(str2cards(case))))
        
    
    def test_flush(self):
        case = "2sAd3s5s7sKs4h"
        self.assertEqual("Flush: Ks7s5s3s2s", str(find_best_hand(str2cards(case))))
        case = "2sAs9s5s7sKs4h"
        self.assertEqual("Flush: AsKs9s7s5s", str(find_best_hand(str2cards(case))))
        case = "2hAhTh5h7hKh4h"
        self.assertEqual("Flush: AhKhTh7h5h", str(find_best_hand(str2cards(case))))
    
    def test_straight(self):
        case = "2sAd3s5h7dKs4h"
        self.assertEqual("Straight: 5h4h3s2sAd", str(find_best_hand(str2cards(case))))
        case = "2sAd3s5h6dKs4h"
        self.assertEqual("Straight: 6d5h4h3s2s", str(find_best_hand(str2cards(case))))
        case = "KsAdQsThJd8s9h"
        self.assertEqual("Straight: AdKsQsJdTh", str(find_best_hand(str2cards(case))))

    def test_three_of_a_kind(self):
        case = "3hAd3s5h3dKs4h"
        self.assertEqual("Three of a Kind: 3s3h3dAdKs", str(find_best_hand(str2cards(case))))
        case = "3hAd7s7h7d2s4h"
        self.assertEqual("Three of a Kind: 7s7h7dAd4h", str(find_best_hand(str2cards(case))))
        case = "KhJdKs5hKdTs4h"
        self.assertEqual("Three of a Kind: KsKhKdJdTs", str(find_best_hand(str2cards(case))))
    
    def test_two_pair(self):
        case = "KhJdJs5hKdTs4h"
        self.assertEqual("Two Pair: KhKdJsJdTs", str(find_best_hand(str2cards(case))))
        case = "KhJdJs5hKdTsTh"
        self.assertEqual("Two Pair: KhKdJsJdTs", str(find_best_hand(str2cards(case))))
        case = "AhJdJs5hKdTsTh"
        self.assertEqual("Two Pair: JsJdTsThAh", str(find_best_hand(str2cards(case))))
        case = "KhJdJs5h9d5s4h"
        self.assertEqual("Two Pair: JsJd5s5hKh", str(find_best_hand(str2cards(case))))
    
    def test_one_pair(self):
        case = "KhJdJs5hAd2sQh"
        self.assertEqual("One Pair: JsJdAdKhQh", str(find_best_hand(str2cards(case))))
        case = "7hJdJs5hAd2sQh"
        self.assertEqual("One Pair: JsJdAdQh7h", str(find_best_hand(str2cards(case))))
        case = "AhTdJs5hAd2sQh"
        self.assertEqual("One Pair: AhAdQhJsTd", str(find_best_hand(str2cards(case))))
    
    def test_high_card(self):
        case = "7hJd8s5hAd2sQh"
        self.assertEqual("High Card: AdQhJd8s7h", str(find_best_hand(str2cards(case))))
        case = "7hJh8s5hAd9sQh"
        self.assertEqual("High Card: AdQhJh9s8s", str(find_best_hand(str2cards(case))))
        
    def test_compare(self):
        h1 = Hand(8, str2cards("AsKsQsJsTs"))
        h2 = Hand(8, str2cards("QsJsTs9s8s"))
        self.assertEqual(-1, compare(h1, h2))       
        h1 = Hand(7, str2cards("AsAhAdAcTs"))
        h2 = Hand(7, str2cards("AsAhAdAc8s"))
        self.assertEqual(-1, compare(h1, h2))       
        h1 = Hand(7, str2cards("KsKhKdKc2s"))
        h2 = Hand(7, str2cards("2s2h2d2cKs"))
        self.assertEqual(-1, compare(h1, h2))
        h1 = Hand(5, str2cards("AsKsQsJs2s"))
        h2 = Hand(5, str2cards("AsKsQsTs8s"))
        self.assertEqual(-1, compare(h1, h2))    
        h1 = Hand(3, str2cards("KsKhKd3c2s"))
        h2 = Hand(3, str2cards("2s2h2dAcKs"))
        self.assertEqual(-1, compare(h1, h2))     
        h1 = Hand(0, str2cards("AsKsQsJs2d"))
        h2 = Hand(0, str2cards("AsKsTs9d8s"))
        self.assertEqual(-1, compare(h1, h2))      
        h1 = Hand(5, str2cards("AsKsQsJs2s"))
        h2 = Hand(0, str2cards("AsKsQsTs8d"))
        self.assertEqual(-1, compare(h1, h2))

def str2cards(s):
    ans =[]
    for j in range(0, floor(len(s) / 2)):
        ans.append(Card(str2code(s[2 * j : 2 * j + 2])))
    return ans


def str2code(s):
    if s[0] == 'A':
        rank = 0
    elif s[0] == 'K':
        rank = 1
    elif s[0] == 'Q':
        rank = 2
    elif s[0] == 'J':
        rank = 3         
    elif s[0] == 'T':
        rank = 4
    elif s[0] == '9':
        rank = 5
    elif s[0] == '8':
        rank = 6
    elif s[0] == '7':
        rank = 7
    elif s[0] == '6':
        rank = 8
    elif s[0] == '5':
        rank = 9
    elif s[0] == '4':
        rank = 10
    elif s[0] == '3':
        rank = 11
    else:
        rank = 12
    code = rank * 4
    if s[1] == 'h':
        code += 1
    elif s[1] == 'd':
        code += 2
    elif s[1] == 'c':
        code += 3
    return code
        

