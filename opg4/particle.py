from config import random, np

class Particle:
    def __init__(self, potentialFunction, alpha, startPos = 0, betak=1000, N_x=100, id = False):
        self.alpha = alpha
        self.id = id
        self.xPos = startPos
        self.time = 0
        self.absxPos = 0
        self.movement = 0
        self.sawtoothPotetial = potentialFunction
        self.constantPotetial = lambda x, alpha, N_x: 1
        self.activePotetial = self.constantPotetial
        self.betak = betak
        self.N_x = N_x

    def pPlus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos - 1, self.alpha, self.N_x)
                                               - self.activePotetial(self.xPos + 1, self.alpha, self.N_x))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos, self.alpha, self.N_x)
                                             - self.activePotetial(self.xPos + 1, self.alpha, self.N_x))))
    
    def pMinus(self):
        return 1 / (1 + np.exp(-self.betak * (self.activePotetial(self.xPos + 1, self.alpha, self.N_x)
                                               - self.activePotetial(self.xPos - 1, self.alpha, self.N_x))) 
                    + np.exp(-self.betak * (self.activePotetial(self.xPos, self.alpha, self.N_x)
                                             - self.activePotetial(self.xPos - 1, self.alpha, self.N_x))))

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
            if self.xPos < -self.N_x:
                self.xPos = self.N_x

        elif prob > 1 - self.pPlus():
            self.movement = 1
            self.xPos += 1
            self.absxPos += 1
            if self.xPos > self.N_x:
                self.xPos = -self.N_x
        else:
            self.movement = 0
        
        return self.absxPos
    
    def getPosition(self):
        return self.xPos
    
    def getProbebility(self):
        return float(self.pMinus()), float(1 - (self.pPlus() + self.pMinus())), float(self.pPlus())

    def __str__(self):
        if self.id:
            return f"{self.id + 1}: {self.xPos}"
        else:
            return f"{self.xPos}"