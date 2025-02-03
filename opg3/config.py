import random
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

def sawtoothPotential(x, alpha): # can only get values between -100 and 100
    if x > -N_x and x <= -(1 - alpha) * N_x:
        return k * (x + N_x) / (alpha * N_x)
    if x > -(1 - alpha) * N_x and x <= 0:
        return - k * x / ((1 - alpha) * N_x)
    if x > 0 and x <= alpha * N_x:
        return k * x / (alpha * N_x)
    if x > alpha * N_x and x <= N_x:
        return - k * (x-N_x) / ((1 - alpha) * N_x)
    else:
        return False
    
N_x = 100 # steps per potetial period
beta_k = 1000
k = 1

if __name__ == "__main__":
    x = np.linspace(-N_x, N_x, 100)
    y = [sawtoothPotential(i, 1) for i in x]
    plt.plot(x, y, 'o')
    plt.grid()
    plt.show()