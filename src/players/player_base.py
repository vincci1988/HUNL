
class PlayerBase:
    
    def __init__(self, pid, balance):
        self.pid = pid
        self.balance = balance
        self.__seat = None
    
    def act(self, status):
        pass
    
    def report(self, final_status):
        pass
    
    def finalize(self):
        pass
    
    def reset(self):
        self.__seat = None