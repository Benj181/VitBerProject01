import random
import numpy as np
import matplotlib.pyplot as plt
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

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

N_x = 100 # steps per potetial period
beta_k = 1000
k = 1

if __name__ == "__main__":
    x = np.linspace(-N_x, N_x, 100)
    y = [sawtoothPotential(i, 1) for i in x]
    plt.plot(x, y, 'o')
    plt.grid()
    plt.show()