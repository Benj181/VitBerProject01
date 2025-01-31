from particle import Particle
from config import *

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
    


alpha = 0.8
T_p = 500 
N_p = N_x * 1
cycles = 10
timeSteps = cycles * 2 * T_p

Particles = [Particle(sawtoothPotential, i, startPos)
              for i, startPos in enumerate(np.linspace(-100, 100, N_p))]

start = time.time()
ParticlesAbsPos = [[] for _ in range(N_p)]

for _ in range(timeSteps): # Iterate over timesteps
    for i, particle in enumerate(Particles): # simulates all particles
        particle.walkStep(T_p)
        ParticlesAbsPos[i].append(particle.absxPos)
        print(f"Simulating particle {i + 1} to {i + 101} at time {round(time.time()-start, 3)} s") if (i + 1) % 100 == 0 else None
        if i % 2 * T_p == 0:
            pass
        # normalizedParticleCurrent = 

print(f"Simulation took {round(time.time()-start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")

for i, Pos in enumerate(ParticlesAbsPos):
    AbsolutePosAxis = np.linspace(0, len(Pos[::400]), len(Pos[::400]))
    plt.plot(AbsolutePosAxis, Pos[::400], markersize=1, label=f"Particle {i + 1}")


# plt.title("Absolute x position of particles")
# plt.xlabel(f"Cycles")
# plt.ylabel("Absolute x position")
# plt.legend()
# plt.show()