from particle import Particle
from config import *
    
start = time.time()
    
N_p = N_x * 1 # 12

T_p = 500 
cycles = 10
timeSteps = cycles * 2 * T_p

    
alpha = 0.8
Particles = [Particle(sawtoothPotential, i, alpha, startPos)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]

normalizedParticleCurrent = []

for i, _ in enumerate(range(timeSteps)): # Iterate over timesteps
    print(f"Simulating timestep {i-999}-{i+1} at time {round(time.time()-start, 3)} s") if (i + 1) % 1000 == 0 else None
    [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
    movementCount = Counter(particle.movement for particle in Particles)
    normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

print(f"Simulation took {round(time.time() - start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")


split_array = np.array_split(normalizedParticleCurrent, cycles)
averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
for i, val in enumerate(averageCurrent):
    print(f"cycle {i+1}: {val:.2e}")  # Adjust decimal places as needed

# ------------------------------------------------------------------------------------
# New alpha value
alpha = 0.1

Particles = [Particle(sawtoothPotential, i, alpha, startPos)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]

for i, _ in enumerate(range(timeSteps)): # Iterate over timesteps
    print(f"Simulating timestep {i-999}-{i+1} at time {round(time.time()-start, 3)} s") if (i + 1) % 1000 == 0 else None
    [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
    movementCount = Counter(particle.movement for particle in Particles)
    normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

print(f"Simulation took {round(time.time() - start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")

split_array = np.array_split(normalizedParticleCurrent, cycles)
averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
for i, val in enumerate(averageCurrent):
    print(f"cycle {i+1}: {val:.2e}")  # Adjust decimal places as needed
