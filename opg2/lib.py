import random
import numpy as np

class Particle:
    def __init__(self, potentialFunction, betak):
        self.x = 0
        self.V = potentialFunction
        self.betak = betak

    def pPlus(self):
        return 1 / (1 + np.exp(-self.betak * (self.V(self.x - 1) - self.V(self.x + 1))) 
                    + np.exp(-self.betak * (self.V(self.x) - self.V(self.x + 1))))
    
    def pMinus(self):
        return 1 / (1 + np.exp(-self.betak * (self.V(self.x + 1) - self.V(self.x - 1))) 
                    + np.exp(-self.betak * (self.V(self.x) - self.V(self.x - 1))))


    def walkStep(self):
        prob = random.uniform(0, 1)
        if prob <= self.pMinus():
            self.x -= 1
        if prob > 1 - self.pPlus():
            self.x += 1
        else:
            self.x = self.x
    
    def getPos(self):
        return self.x
    
    def getProb(self):
        return float(self.pMinus()), float(1 - (self.pPlus() + self.pMinus())), float(self.pPlus())
    