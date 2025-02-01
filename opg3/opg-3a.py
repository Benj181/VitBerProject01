from particle import Particle
from config import *

    
alpha = 0.1
T_p = 200 # time steps per time interval
N_p = 3 # number of particles
cycles = 75
timeSteps = cycles * 2 * T_p

Particles = [Particle(sawtoothPotential, i, alpha) for i, _ in enumerate(range(N_p))]
ParticlesAbsPos = [[] for _ in range(N_p)]
for i, particle in enumerate(Particles): # simulates all particles
    ParticlesAbsPos[i] = [particle.walkStep(T_p) for _ in range(timeSteps)] # run walkstep [simulation] for all
                                                                            # particles and store the absolute position    

for i, Pos in enumerate(ParticlesAbsPos): # plots each particles absolute position
    AbsolutePosAxis = np.linspace(0, len(Pos[::400]), len(Pos[::400]))
    plt.plot(AbsolutePosAxis, Pos[::400], markersize=1, label=f"Particle {i + 1}")

plt.title("Absolute x position of particles")
plt.xlabel(f"Cycles")
plt.ylabel("Absolute x position")
plt.legend()
plt.show()