import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random

class Particle:
    def __init__(self, potentialFunction, betak, id):
        self.id = id
        self.xPos = 0
        self.time = 0
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
            if self.xPos < -100:
                self.xPos = 100

        if prob > 1 - self.pPlus():
            self.xPos += 1
            if self.xPos > 100:
                self.xPos = -100
        else:
            self.xPos = self.xPos
    
        if self.time % (2*T_p) == 0: # every 400 time steps return True (record pos in main)
            return True
        
    def getPosition(self):
        return self.xPos
    
    def getProbebility(self):
        return float(self.pMinus()), float(1 - (self.pPlus() + self.pMinus())), float(self.pPlus())

    def __str__(self):
        return f"{self.id + 1}"

def sawtoothPotential(x): # can only get values between -100 and 100
    if x < -90 and x >= -100:
        return k * x / (alpha * N_x) + k*10
    elif x < 0 and x >= -90:
        return - k * x / ((1 - alpha) * N_x)
    elif x < 10 and x >= 0:
        return k * x / (alpha * N_x)
    elif x <= 100 and x >= 10:
        return - k * x / ((1 - alpha) * N_x) + k*10 / 9
    else:
        return False

T_p = 200 # time steps per time interval
N_p = 3 # number of particles
N_x = 100 # steps per potetial period
beta_k = 1000
cycles = 75
timeSteps = cycles * 2 * T_p
alpha = 0.1
k = 1

cycleAxis = np.linspace(0, cycles, cycles + 1)

Particles = [Particle(sawtoothPotential, beta_k, i) for i, _ in enumerate(range(N_p))]

for particle in Particles: # simulates all particles
    PositionEndCycle = [0]
    for i, _ in enumerate(range(timeSteps)): # run walkstep (simulation) for all timesteps 
        if particle.walkStep(T_p):
            PositionEndCycle.append(particle.getPosition())        
    plt.plot(cycleAxis, PositionEndCycle, 'o', label=f"Particle {particle}")

plt.title("Position of particles at end of cycle")
plt.xlabel("Cycle")
plt.ylabel("Position on x-axis")
plt.show()

# test = [0] # plot every time step
# for i, _ in enumerate(range(timeSteps)):
#     for particle in Particles:
#         particle.walkStep(T_p)
#         test.append(particle.getPosition())
#         break
# testAxis = np.linspace(0, timeSteps, timeSteps + 1)
# plt.plot(testAxis, test, 'ro', markersize=1)
# plt.show()