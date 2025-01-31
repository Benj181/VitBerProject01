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
    
alpha = 0.1
T_p = 200 # time steps per time interval
N_p = 3 # number of particles
cycles = 75
timeSteps = cycles * 2 * T_p

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