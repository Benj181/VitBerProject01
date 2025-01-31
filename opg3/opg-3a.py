from particle import Particle
from functions import sawtoothPotential
from config import *

Particles = [Particle(sawtoothPotential, i) for i, _ in enumerate(range(N_p))]
ParticlesAbsPos = [[] for _ in range(N_p)] # [[], [], []]
for i, particle in enumerate(Particles): # simulates all particles
    for _ in range(timeSteps): # run walkstep [simulation] for all timesteps 
        particle.walkStep(T_p)
        ParticlesAbsPos[i].append(particle.absxPos)


for i, Pos in enumerate(ParticlesAbsPos):
    AbsolutePosAxis = np.linspace(0, len(Pos[::400]), len(Pos[::400]))
    plt.plot(AbsolutePosAxis, Pos[::400], markersize=1, label=f"Particle {i + 1}")

plt.title("Absolute x position of particles")
plt.xlabel(f"Cycles")
plt.ylabel("Absolute x position")
plt.legend()
plt.show()



# plt.xticks(np.arange(0, cycles, 1))
# plt.gca().set_xticklabels([])
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)