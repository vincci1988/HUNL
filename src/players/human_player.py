from src.players.player_base import PlayerBase

class HumanPlayer(PlayerBase):
    
    def __init__(self, pid, balance):
        self.pid = pid
        self.balance = balance
        
    def __str__(self):
        return "Human Player[{}]".format(self.pid)
    
    def act(self, status):
        print(self.__str__())
        print(f"Status: {status}")
        return input("Action: ")
    
    def report(self, final_status):
        print(self.__str__())
        print(f"Final Status: {final_status}")
        return final_status
    
    def finalize(self):
        print( self.__str__() + f"\nCurrent Balance: {self.balance}")