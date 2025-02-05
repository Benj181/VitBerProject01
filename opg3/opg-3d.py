from particle import Particle
from config import *

T_p = 500
N_p = N_x * 12
averageCurrent = []
normalizedParticleCurrent = []
startPosistions = [0] * ( N_p // 2) + [100] * (N_p // 2)
alphaList = np.linspace(0, 1, 50) # 50
for alpha in progressBar(alphaList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different alphas
    Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPosistions]
    for _ in range(int(2 * T_p )): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p) # calculate current
    averageCurrent.append(float(np.mean(normalizedParticleCurrent))) # avg current per alpha
    normalizedParticleCurrent.clear()

plt.plot(alphaList, averageCurrent)
plt.xlabel("Alpha")
plt.ylabel("Average current")
plt.title("Average current over different Alpha")
plt.grid()
plt.show()