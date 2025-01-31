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
    
    

alpha = 0.8
N_p = N_x * 1 # 40

normalizedParticleCurrent = []
averageCurrent = []
T_pList = np.linspace(1, 1001, 50)
start = time.time()
for i, T_p in enumerate(T_pList): # Iterate over different timeintervals
    Particles = [Particle(sawtoothPotential, i, startPos, alpha)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]
    temp = time.time()
    # print(f"{i}: Simulating for {int(2*T_p)} as T_p")
    for i, _ in enumerate(range(int(2 * T_p ))): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)
    # print(f"Simulation took {round(time.time() - temp, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")
    # print("-------------------------------------------")
    averageCurrent.append(float(np.mean(normalizedParticleCurrent)))

print(f"Total time: {round(time.time() - start, 2)} s")

averageCurrent.pop(0)   
T_pList = T_pList[1:]

plt.plot(T_pList, averageCurrent)
plt.xlabel("T_p")
plt.ylabel("Average current")
plt.title("Average current over different T_p")
plt.grid()
plt.show()