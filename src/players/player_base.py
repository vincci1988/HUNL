from abc import abstractmethod


class PlayerBase:
    
    def __init__(self, pid, balance):
        self.pid = pid
        self.balance = balance
        self.seat = None
    
    @abstractmethod
    def act(self, status):
        pass
    
    @abstractmethod
    def report(self, final_status):
        pass
    
    @abstractmethod
    def finalize(self):
        pass