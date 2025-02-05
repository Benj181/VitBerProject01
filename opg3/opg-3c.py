from particle import Particle
from config import *

alpha = 0.8
N_p = N_x * 40
averageCurrent = []
normalizedParticleCurrent = []
startPosistions = [0] * ( N_p // 2) + [100] * (N_p // 2)
T_pList = np.linspace(1, 1001, 50).astype(int)
for T_p in progressBar(T_pList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different timeintervals: 
    Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPosistions]   
    for i, _ in enumerate(range(int(2 * T_p ))): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)
    averageCurrent.append(float(np.mean(normalizedParticleCurrent)))  # avg current per T_p
    normalizedParticleCurrent.clear()

plt.plot(T_pList, averageCurrent)
plt.xlabel("T_p")
plt.ylabel("Average current")
plt.title("Average current over different T_p")
plt.grid()
plt.show()