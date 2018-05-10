from src.exp.holdem_judges import find_best_hand
from src.exp.holdem_judges import compare
from src.exp.playing_cards import Deck
from src.players.player_base import PlayerBase


class HUNLTable:
    
    PLAYER_CNT = 2
    DEFAULT_SB = 50
    DEFAULT_BB = 100
    DEFAULT_STK = 20000
    
    def __init__(self):
        self.seats = [_Seat(), _Seat()]
        self.button = 0
        self.__reset()
        self.SB = HUNLTable.DEFAULT_SB
        self.BB = HUNLTable.DEFAULT_BB
        self.STK = HUNLTable.DEFAULT_STK
        
    def std_match(self, player1, player2, game_cnt = 1, duplicated = False):
        if not (isinstance(player1, PlayerBase) and isinstance(player2, PlayerBase)):
            raise TypeError("HUNLTable.std_match: Player type")
        if game_cnt < 1:
            raise ValueError("HUNLTable.std_match: Invalid game_cnt")
        decks = []
        for _ in range(0, game_cnt):
            deck = Deck()
            deck.shuffle_deck()
            decks.append(deck)                        
        self.__seat(player1)
        self.__seat(player2)
        for j in range(0, game_cnt):
            self.__std_game(decks[j])
        self.__clear()
        if duplicated:
            self.__seat(player2)
            self.__seat(player1)
            for j in range(0, game_cnt):
                decks[j].reset()
                self.__std_game(decks[j])
            self.__clear()
    
    def __seat(self, player):
        if self.seats[0].player == None:
            self.seats[0].player = player
        elif self.seats[1].player == None:
            self.seats[1].player = player
        else:
            raise IndexError("HUNLTable.__seat: Full table")
    
    def __std_game(self, deck):
        self.__reset()
        self.seats[0].buy_in(self.STK)
        self.seats[1].buy_in(self.STK)        
        self.button = (self.button + 1) % HUNLTable.PLAYER_CNT
        bb = (self.button + 1) % HUNLTable.PLAYER_CNT
        # blinds
        self.seats[self.button].post(self.SB)
        self.seats[bb].post(self.BB)
        # deal
        for _ in range(0, HUNLTable.PLAYER_CNT):
            self.seats[bb].hole_cards.append(deck.next_card())
            self.seats[self.button].hole_cards.append(deck.next_card())
        # preflop
        self.__bet(self.button)
        if len(self.winner) > 0:
            self.__win_before_showdown()
        # flop
        if len(self.winner) == 0:
            self.actions += '/'
            for _ in range(0, 3):
                self.board.append(deck.next_card())
            if not self.__players_all_in():
                self.__bet(bb)
            if len(self.winner) > 0:
                self.__win_before_showdown()
        # turn
        if len(self.winner) == 0:
            self.actions += '/'
            self.board.append(deck.next_card())
            if not self.__players_all_in():
                self.__bet(bb)
            if len(self.winner) > 0:
                self.__win_before_showdown()
        # river
        if len(self.winner) == 0:
            self.actions += '/'
            self.board.append(deck.next_card())
            if not self.__players_all_in():
                self.__bet(bb)
            if len(self.winner) == 0:
                self.__showdown()
            else:
                self.__win_before_showdown()
        self.seats[0].return_hole_cards()
        self.seats[1].return_hole_cards()
        self.seats[0].cash_out()
        self.seats[1].cash_out()
    
    def __clear(self):
        self.seats[0].detach()
        self.seats[1].detach()
        self.__reset()
        self.button = 0
    
    def __reset(self):
        self.board = []
        self.pot = 0
        self.actions = ""
        self.winner = []
        
    def __bet(self, next_to_act):
        action_cnt = 0
        minBet = self.BB
        while action_cnt < 2 or self.seats[0].bet != self.seats[1].bet:
            action_cnt += 1
            other = (next_to_act + 1) % HUNLTable.PLAYER_CNT
            act = self.seats[next_to_act].act(self.__get_status(next_to_act))
            # 'f' = fold, 'k' = check, 'c' = call, 'r' = bet/raise
            if not self.__check(act, next_to_act, minBet): 
                if self.seats[next_to_act].bet == self.seats[other].bet: 
                    act = 'k'
                else:
                    act = 'f' 
            self.actions += act
            if act == 'f':
                self.winner.append(self.seats[other])
                break
            elif act == 'c':
                self.seats[next_to_act].post(self.seats[other].bet - self.seats[next_to_act].bet)
            elif act[0] == 'r':
                amt = int(act[1:])
                minBet = amt - self.seats[other].bet
                self.seats[next_to_act].post(amt - self.seats[next_to_act].bet)
            next_to_act = other
        self.__collect()
        
    def __win_before_showdown(self):
        self.seats[0].report(self.__get_status(0))
        self.seats[1].report(self.__get_status(1))
        self.__ship()
        
    def __showdown(self):
        self.seats[0].report(self.__get_status(0, True))
        self.seats[1].report(self.__get_status(1, True))
        h0 = find_best_hand(self.seats[0].hole_cards + self.board)
        h1 = find_best_hand(self.seats[1].hole_cards + self.board)
        res = compare(h0, h1) 
        if res == 0:
            self.winner += self.seats
        elif res == -1:
            self.winner.append(self.seats[0])
        else:
            self.winner.append(self.seats[1])
        self.__ship()
    
    def __ship(self):
        for w in self.winner:
            w.stack += int(self.pot / len(self.winner))
    
    def __players_all_in(self):
        return self.seats[0].stack == 0 or self.seats[1].stack == 0
    
    def __get_status(self, j, showdown = False):
        prvt = "".join([str(card) for card in self.seats[j].hole_cards])
        if showdown:
            prvt += "/" + "".join([str(card) for card in self.seats[(j + 1) % HUNLTable.PLAYER_CNT].hole_cards])
        else:
            prvt += "/XxXx"
        pblc = "".join([str(card) for card in self.board]) + ":" + self.actions
        return prvt + ":" + pblc
    
    def __check(self, act, me, minBet):
        opponent = (me + 1) % HUNLTable.PLAYER_CNT
        if act == 'f':
            return self.seats[me].bet < self.seats[opponent].bet
        if act == 'k':
            return self.seats[opponent].bet == self.seats[me].bet
        if act == 'c':
            return self.seats[opponent].bet > self.seats[me].bet
        if act[0:1] == 'r':
            if self.seats[opponent].bet - self.seats[me].bet >= self.seats[me].stack:
                return False
            amt = int(act[1:])
            if amt - self.seats[me].bet > self.seats[me].stack:
                return False
            if amt - self.seats[opponent].bet < minBet and amt - self.seats[me].bet < self.seats[me].stack:
                return False
            return True
        return False
        
    def __collect(self):
        self.pot += self.seats[0].bet + self.seats[1].bet
        self.seats[0].bet = 0
        self.seats[1].bet = 0

   
class _Seat:
    
    def __init__(self):
        self.hole_cards = []
        self.stack = 0
        self.bet = 0
        self.player = None
    
    def buy_in(self, amt):
        if self.player != None:
            self.player.balance -= amt
            self.stack += amt
            self.bet = 0
        else:
            raise ValueError("_Seat.buy_in: Empty __seat")
    
    def cash_out(self):
        if self.player != None:
            self.player.balance += self.stack
            self.stack = 0
            self.bet = 0
            self.player.finalize()
        else:
            raise ValueError("_Seat.buy_in: Empty __seat") 
    
    def detach(self):
        self.player.reset()
        self.player = None
    
    def post(self, amt):
        if amt > self.stack:
            amt = self.stack
        elif amt < 0:
            amt = 0
        self.stack -= amt
        self.bet += amt
    
    def return_hole_cards(self):
        self.hole_cards = []
        
    def act(self, status):
        return self.player.act(status)
    
    def report(self, final_status):
        self.player.report(final_status)

