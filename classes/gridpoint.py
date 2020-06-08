import numpy as np
class gridpoint:
    
    def __init__(self, location : int, numresources : int, numlocusts : int):
        self.location = location
        self.resources = numresources
        self.locusts = numlocusts
    
    def newlocust(self):
        self.locusts += 1
    
    def loselocust(self):
        self.locusts -= 1
    
    def gainfood(self):
        self.resources += 1
    
    def losefood(self):
        self.resources -= 1

    def hasfood(self) -> bool:
        if self.resources > 0:
            return True
        else:
            return False
    
    def getlocusts(self) -> int:
        return self.locusts
    


