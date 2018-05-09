
class Hand:
    
    def __init__(self, rank, cards):
        self.rank = rank
        self.cards = cards
    
    def __str__(self):
        if self.rank == 0:
            ans = 'High Card'
        elif self.rank == 1:
            ans = 'One Pair'
        elif self.rank == 2:
            ans = 'Two Pair'
        elif self.rank == 3:
            ans = 'Three of a Kind'
        elif self.rank == 4:
            ans = 'Straight'
        elif self.rank == 5:
            ans = 'Flush'
        elif self.rank == 6:
            ans = 'Full House'
        elif self.rank == 7:
            ans = 'Four of a Kind'
        else:
            ans = 'Straight Flush'
        ans += ": " 
        for card in self.cards:
            ans += str(card)
        return ans      


def compare(hand1, hand2):
    if hand1.rank > hand2.rank:
        return -1
    if hand1.rank < hand2.rank:
        return 1
    for j in range(0, 5):
        if hand1.cards[j].getNumRank() < hand2.cards[j].getNumRank():
            return -1
        if hand1.cards[j].getNumRank() > hand2.cards[j].getNumRank():
            return 1    
    return 0

def find_best_hand(cards):
    cards.sort(key = lambda card: card.code)
    fv = __flush_analyze(cards)
    rv = __rank_analyze(cards)   
    sf = __str8_analyze(fv)
    if sf != None:
        return Hand(8, sf)  #straight flush
    if len(rv[0]) == 4:
        if rv[0][0].getNumRank() == cards[0].getNumRank():
            return Hand(7, rv[0] + cards[4 : 5]) # four of a kind
        else:
            return Hand(7, rv[0] + cards[0 : 1]) 
    if len(rv[0]) == 3 and len(rv[1]) >= 2: 
        return Hand(6, rv[0] + rv[1][0 : 2]) # full house
    if fv != None:
        return Hand(5, fv[0 : 5]) # flush
    sv = __str8_analyze(cards) 
    if sv != None:
        return Hand(4, sv) # straight
    if len(rv[0]) == 3:
        return Hand(3, rv[0] + rv[1] + rv[2]) # three of a kind
    if len(rv[0]) == 2 and len(rv[1]) == 2:
        for card in cards:
            r = card.getNumRank()
            if r != rv[0][0].getNumRank() and r != rv[1][0].getNumRank():
                return Hand(2, rv[0] + rv[1] + [card]) # two pair
    if len(rv[0]) == 2:
        return Hand(1, rv[0] + rv[1] + rv[2] + rv[3]) # one pair
    return Hand(0, cards[:5]) # high card


def __rank_analyze(cards):
    rank_view = [[cards[0]]]
    for j in range(1, len(cards)):
        if cards[j].getNumRank() == rank_view[-1][0].getNumRank():
            rank_view[-1].append(cards[j])
        else:
            rank_view.append([cards[j]])
    rank_view.sort(key=lambda rank : len(rank), reverse = True)
    return rank_view

    
def __flush_analyze(cards):
    flush_view = [[], [], [], []]
    for card in cards:
        flush_view[card.getNumSuit()].append(card)
    for suit in flush_view:
        if len(suit) >= 5:
            return suit
    return None

    
def __str8_analyze(cards):
    if cards == None:
        return None
    ans = [cards[0]]
    for j in range(1, len(cards)):
        if cards[j].getNumRank() - 1 == ans[-1].getNumRank():
            ans.append(cards[j])
            if len(ans) == 5:
                return ans
        elif cards[j].getNumRank() - 1 > ans[-1].getNumRank():
            ans = [cards[j]]
    if cards[0].getNumRank() == 0 and len(ans) == 4 and ans[-1].getNumRank() == 12:
        ans.append(cards[0])
        return ans
    return None
