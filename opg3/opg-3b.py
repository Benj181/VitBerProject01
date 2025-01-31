from particle import Particle
from functions import sawtoothPotential
from config import *

alpha = 0.8
T_p = 500 
N_p = N_x * 1
Particles = [Particle(sawtoothPotential, i, startPos)
              for i, startPos in enumerate(np.linspace(-100, 100, N_p))]

start = time.time()
ParticlesAbsPos = [[] for _ in range(N_p)]
for i, particle in enumerate(Particles): # simulates all particles
    print(f"Simulating particle {i + 1} to {i + 101} at time {round(time.time()-start, 3)} s") if (i + 1) % 100 == 0 else None
    if i % 2 * T_p == 0:
        pass
    for _ in range(timeSteps): # run walkstep (simulation) for all timesteps 
        particle.walkStep(T_p)
        ParticlesAbsPos[i].append(particle.absxPos)

print(f"Simulation took {round(time.time()-start, 2)} s with average time per particle {round((time.time()-start)*1000/N_p, 1)} ms")

for i, Pos in enumerate(ParticlesAbsPos):
    AbsolutePosAxis = np.linspace(0, len(Pos[::400]), len(Pos[::400]))
    plt.plot(AbsolutePosAxis, Pos[::400], markersize=1, label=f"Particle {i + 1}")


# plt.title("Absolute x position of particles")
# plt.xlabel(f"Cycles")
# plt.ylabel("Absolute x position")
# plt.legend()
# plt.show()