from config import random, np

class Particle:
    def __init__(self, potentialFunction, betak, id):
        self.id = id
        self.xPos = 0
        self.time = 0
        self.absxPos = 0
        self.sawtoothPotetial = potentialFunction
        self.constantPotetial = lambda x: 1
        self.activePotetial = self.constantPotetial
        self.betak = betak

    def pPlus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos - 1)
                                               - self.activePotetial(self.xPos + 1))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos)
                                             - self.activePotetial(self.xPos + 1))))
    
    def pMinus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos + 1)
                                               - self.activePotetial(self.xPos - 1))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos)
                                             - self.activePotetial(self.xPos - 1))))

    def potentialSwitch(self):
        if self.activePotetial == self.constantPotetial:
            self.activePotetial = self.sawtoothPotetial
        else:
            self.activePotetial = self.constantPotetial

    def walkStep(self, T_p):
        self.time += 1

        if self.time % T_p == 0: # every 200 time steps switch potential
            self.potentialSwitch()
        
        prob = random.uniform(0, 1)
        if prob <= self.pMinus():
            self.xPos -= 1
            self.absxPos -= 1
            if self.xPos < -100:
                self.xPos = 100

        elif prob > 1 - self.pPlus():
            self.xPos += 1
            self.absxPos += 1
            if self.xPos > 100:
                self.xPos = -100
        
    def getPosition(self):
        return self.xPos
    
    def getProbebility(self):
        return float(self.pMinus()), float(1 - (self.pPlus() + self.pMinus())), float(self.pPlus())

    def __str__(self):
        return f"{self.id + 1}"