from config import random, np, beta_k

class Particle:
    def __init__(self, potentialFunction, id, alpha, startPos = 0):
        self.alpha = alpha
        self.id = id
        self.xPos = startPos
        self.time = 0
        self.absxPos = 0
        self.movement = 0
        self.sawtoothPotetial = potentialFunction
        self.constantPotetial = lambda x, alpha: 1
        self.activePotetial = self.constantPotetial
        self.betak = beta_k

    def pPlus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos - 1, self.alpha)
                                               - self.activePotetial(self.xPos + 1, self.alpha))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos, self.alpha)
                                             - self.activePotetial(self.xPos + 1, self.alpha))))
    
    def pMinus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos + 1, self.alpha)
                                               - self.activePotetial(self.xPos - 1, self.alpha))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos, self.alpha)
                                             - self.activePotetial(self.xPos - 1, self.alpha))))

    def potentialSwitch(self):
        if self.activePotetial == self.constantPotetial:
            self.activePotetial = self.sawtoothPotetial
        else:
            self.activePotetial = self.constantPotetial

    def walkStep(self, T_p):
        self.time += 1

        if self.time % T_p == 0:
            self.potentialSwitch()
        
        prob = random.uniform(0, 1)
        if prob <= self.pMinus():
            self.movement = -1
            self.xPos -= 1
            self.absxPos -= 1
            if self.xPos < -100:
                self.xPos = 100

        elif prob > 1 - self.pPlus():
            self.movement = 1
            self.xPos += 1
            self.absxPos += 1
            if self.xPos > 100:
                self.xPos = -100
        else:
            self.movement = 0
        
        return self.absxPos
    
    def getPosition(self):
        return self.xPos
    
    def getProbebility(self):
        return float(self.pMinus()), float(1 - (self.pPlus() + self.pMinus())), float(self.pPlus())

    def __str__(self):
        return f"{self.id + 1}"