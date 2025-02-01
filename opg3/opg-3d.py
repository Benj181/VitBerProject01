from particle import Particle
from config import *

start = time.time()

T_p = 500
N_p = N_x * 1 # 12


normalizedParticleCurrent = []
averageCurrent = []

alphaList = np.linspace(0, 1, 10) # 50

for i, alpha in enumerate(alphaList): # Iterate over different alphas
    Particles = [Particle(sawtoothPotential, i, alpha, startPos)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))] # make list of particles
    temp = time.time()

    print(f"{i}: Simulating for {round(alpha, 2)} as alpha")
    for i, _ in enumerate(range(int(2 * T_p ))): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p) # calculate current
    print(f"Simulation took {round(time.time() - temp, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")
    print("-------------------------------------------")
    averageCurrent.append(float(np.mean(normalizedParticleCurrent))) # avg current per alpha

print(f"Total time: {round(time.time() - start, 2)} s")


plt.plot(alphaList, averageCurrent)
plt.xlabel("Alpha")
plt.ylabel("Average current")
plt.title("Average current over different Alpha")
plt.grid()
plt.show()