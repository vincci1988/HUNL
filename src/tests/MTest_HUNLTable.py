from src.exp.game_table import HUNLTable
from src.players.human_player import HumanPlayer
from src.exp.playing_cards import Deck

def manual_test():
    t = HUNLTable()
    deck = Deck()
    deposit_amt = 1000000
    t.seat(HumanPlayer(0, deposit_amt))
    t.seat(HumanPlayer(1, deposit_amt))
    while True:
        deck.shuffle_deck() 
        t.std_game(deck)
        s = input("Would you like to test with another hand? (Y/N)\n")
        if s != 'Y':
            break

        
if __name__ == '__main__':
    manual_test()