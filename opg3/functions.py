from config import k, alpha, N_x

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