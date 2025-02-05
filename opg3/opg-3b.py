from particle import Particle
from config import *
    
N_p = N_x * 12

T_p = 500 
cycles = 10
timeSteps = cycles * 2 * T_p
startPositons = np.linspace(-N_x, N_x, N_p)
normalizedParticleCurrent = []

alpha = 0.8
Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPositons]
for _ in progressBar(range(timeSteps), prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over timesteps
    [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
    movementCount = Counter(particle.movement for particle in Particles)
    normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

split_array = np.array_split(normalizedParticleCurrent, cycles)
averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
for i, val in enumerate(averageCurrent):
    print(f"cycle {i+1}: {val:.2e}") 

# ------------------------------------------------------------------------------------
# New alpha value
alpha = 0.1
Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPositons]
normalizedParticleCurrent.clear()
for _ in progressBar(range(timeSteps), prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over timesteps
    [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
    movementCount = Counter(particle.movement for particle in Particles)
    normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

split_array = np.array_split(normalizedParticleCurrent, cycles)
averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
for i, val in enumerate(averageCurrent):
    print(f"cycle {i+1}: {val:.2e}")  # Adjust decimal places as needed
