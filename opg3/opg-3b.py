from particle import Particle
from config import *


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


start = time.time()
    
N_p = N_x * 1 # 12

T_p = 500 
cycles = 10
timeSteps = cycles * 2 * T_p

    
alpha = 0.8
Particles = [Particle(sawtoothPotential, i, alpha, startPos)
              for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]

normalizedParticleCurrent = []
printProgressBar(0, timeSteps, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, _ in enumerate(range(timeSteps)): # Iterate over timesteps
    # print(f"Simulating timestep {i + 1} at time {round(time.time()-start, 3)} s") if (i + 1) % 1000 == 0 else None
    [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
    movementCount = Counter(particle.movement for particle in Particles)
    normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

    printProgressBar(i, timeSteps, prefix = 'Progress:', suffix = 'Complete', length = 50)


print(f"Simulation took {round(time.time() - start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")


split_array = np.array_split(normalizedParticleCurrent, cycles)
averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
for i, val in enumerate(averageCurrent):
    print(f"cycle {i+1}: {val:.2e}") 

# ------------------------------------------------------------------------------------
# # New alpha value
# alpha = 0.1

# Particles = [Particle(sawtoothPotential, i, alpha, startPos)
#               for i, startPos in enumerate(np.linspace(-N_x, N_x, N_p))]

# for i, _ in enumerate(range(timeSteps)): # Iterate over timesteps
#     print(f"Simulating timestep {i + 1} at time {round(time.time()-start, 3)} s") if (i + 1) % 1000 == 0 else None
#     [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
#     movementCount = Counter(particle.movement for particle in Particles)
#     normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

# print(f"Simulation took {round(time.time() - start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")

# split_array = np.array_split(normalizedParticleCurrent, cycles)
# averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle
# for i, val in enumerate(averageCurrent):
#     print(f"cycle {i+1}: {val:.2e}")  # Adjust decimal places as needed
