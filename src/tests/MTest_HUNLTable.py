from src.exp.game_table import HUNLTable
from src.players.human_player import HumanPlayer

def manual_test():
    t = HUNLTable()
    game_cnt = int(input("How many hand(s) would you like to play?\n"))
    deposit_amt = 1000000
    t.std_match(HumanPlayer(0, deposit_amt), HumanPlayer(1, deposit_amt), game_cnt, True)

        
if __name__ == '__main__':
    manual_test()