from config import k, alpha, N_x

def sawtoothPotential(x): # can only get values between -100 and 100
    if x >= -N_x and x < -(1 - alpha) * N_x:
        return k * (x + N_x) / (alpha * N_x)
    if x >= -(1 - alpha) * N_x and x < 0:
        return - k * x / ((1 - alpha) * N_x)
    if x >= 0 and x < alpha * N_x:
        return k * x / (alpha * N_x)
    if x >= alpha * N_x and x <= 100:
        return - k * (x-N_x) / ((1 - alpha) * N_x)
    else:
        return False

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(-100, 100, 1000)
    y = [sawtoothPotential(i) for i in x]
    plt.plot(x, y)
    plt.title("Sawtooth potential")
    plt.xlabel("x")
    plt.ylabel("V(x)")
    plt.show()