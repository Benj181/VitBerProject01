from particle import Particle
from config import *

def sawtoothPotential(x, alpha): # can only get values between -100 and 100
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
    

T_p = 500
N_p = N_x * 1 # 12


normalizedParticleCurrent = []
averageCurrent = []
alphaList = np.linspace(0, 1, 50)
start = time.time()
for i, alpha in enumerate(alphaList): # Iterate over different alphas
    Particles = [Particle(sawtoothPotential, i, startPos, alpha)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]
    temp = time.time()
    print(f"{i}: Simulating for {alpha} as alpha")
    for i, _ in enumerate(range(int(2 * T_p ))): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)
    print(f"Simulation took {round(time.time() - temp, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")
    print("-------------------------------------------")
    averageCurrent.append(float(np.mean(normalizedParticleCurrent)))

print(f"Total time: {round(time.time() - start, 2)} s")


plt.plot(alphaList, averageCurrent)
plt.xlabel("T_p")
plt.ylabel("Average current")
plt.title("Average current over different T_p")
plt.grid()
plt.show()