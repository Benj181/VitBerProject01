from config import *
from particle import Particle
import os
import sys

def analyticalAverageCurrent(alpha, T_p, N_x):
    return N_x / (4 * T_p) * (erfc(alpha * N_x / 2 * np.sqrt(3/T_p)) - erfc((1-alpha) * N_x / 2 * np.sqrt(3/T_p)))

def opg3aSim():
    alpha = 0.1
    T_p = 200
    N_p = 3
    cycles = 75
    timeSteps = cycles * 2 * T_p

    Particles = [Particle(sawtoothPotential, alpha) for _ in range(N_p)]
    ParticlesAbsPos = [[] for _ in range(N_p)]
    for i, particle in enumerate(Particles): # simulates all particles
        ParticlesAbsPos[i] = [particle.walkStep(T_p) for _ in range(timeSteps)] # run walkstep [simulation] for all
                                                                                # particles and store the absolute position    
    return ParticlesAbsPos

def opg3bSim(alpha, N_p):
    T_p = 500 
    cycles = 10
    timeSteps = cycles * 2 * T_p
    startPositons = np.linspace(-N_x, N_x, N_p)
    normalizedParticleCurrent = []

    Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPositons]
    for _ in progressBar(range(timeSteps), prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over timesteps
        [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
        movementCount = Counter(particle.movement for particle in Particles)
        normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)

    split_array = np.array_split(normalizedParticleCurrent, cycles)
    averageCurrent = [float(np.mean(part)) for part in split_array] # average current per cycle

    return averageCurrent

def opg3cSim(N_p):
    alpha = 0.8
    averageCurrent = []
    normalizedParticleCurrent = []
    startPosistions = [0] * ( N_p // 2) + [100] * (N_p // 2)
    T_pList = np.linspace(1, 1001, 50).astype(int)
    for T_p in progressBar(T_pList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different timeintervals: 
        Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPosistions]   
        for _ in range(int(2 * T_p )): # Iterate over timesteps
            [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
            movementCount = Counter(particle.movement for particle in Particles)
            normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)
        averageCurrent.append(float(np.mean(normalizedParticleCurrent)))  # avg current per T_p
        normalizedParticleCurrent.clear()
    return T_pList, averageCurrent

def opg3dSim(N_p):
    T_p = 500
    averageCurrent = []
    normalizedParticleCurrent = []
    startPosistions = [0] * ( N_p // 2) + [100] * (N_p // 2)
    alphaList = np.linspace(0, 1, 50)
    for alpha in progressBar(alphaList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different alphas
        Particles = [Particle(sawtoothPotential, alpha, startPos) for startPos in startPosistions]
        for _ in range(int(2 * T_p )): # Iterate over timesteps
            [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
            movementCount = Counter(particle.movement for particle in Particles)
            normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p) # calculate current
        averageCurrent.append(float(np.mean(normalizedParticleCurrent))) # avg current per alpha
        normalizedParticleCurrent.clear()

    return alphaList, averageCurrent

def opg4bSim(N_p, N_x, T_pList):
    alpha = 0.8
    averageCurrent = []
    normalizedParticleCurrent = []
    startPosistions = [0] * ( N_p // 2) + [N_x] * (N_p // 2)
    for T_p in progressBar(T_pList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different timeintervals: 
        Particles = [Particle(sawtoothPotential, alpha, startPos, N_x=N_x) for startPos in startPosistions] 
        for _ in range(int(2 * T_p )): # Iterate over timesteps 
            [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
            movementCount = Counter(particle.movement for particle in Particles)
            normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p)
        averageCurrent.append(float(np.mean(normalizedParticleCurrent)))  # avg current per T_p
        normalizedParticleCurrent.clear()
    return averageCurrent

def opg4cSim(N_p, betak):
    T_p = 500
    averageCurrent = []
    normalizedParticleCurrent = []
    startPosistions = [0] * ( N_p // 2) + [100] * (N_p // 2)
    alphaList = np.linspace(0, 1, 50)
    for alpha in progressBar(alphaList, prefix = 'Progress:', suffix = 'Complete', length = 50): # Iterate over different alphas
        Particles = [Particle(sawtoothPotential, alpha, startPos, betak) for startPos in startPosistions]
        for _ in range(int(2 * T_p )): # Iterate over timesteps
            [particle.walkStep(T_p) for particle in Particles] # runs sim for every particle
            movementCount = Counter(particle.movement for particle in Particles)
            normalizedParticleCurrent.append((movementCount[1] - movementCount[-1]) / N_p) # calculate current
        averageCurrent.append(float(np.mean(normalizedParticleCurrent))) # avg current per alpha
        normalizedParticleCurrent.clear()

    return alphaList, averageCurrent

def generateData(N_p, opg3b=False, opg3c=False, opg3d=False, opg4b=False, opg4c=False):
    if opg3b:
        print("Running opg3b")
        averageCurrent01 = opg3bSim(0.1, N_p)
        averageCurrent02 = opg3bSim(0.8, N_p) 
        with open('data\\results_opg3b.txt', 'w') as file:
            file.write("averageCurrent01:\n")
            file.write("\n".join(map(str, averageCurrent01)) + "\n")
            file.write("averageCurrent02:\n")
            file.write("\n".join(map(str, averageCurrent02)) + "\n")

    if opg3c:
        print("Running opg3c")
        T_pList, averageCurrent = opg3cSim(N_p) 
        with open('data\\results_opg3c.txt', 'w') as file:
            file.write("T_pList and averageCurrent:\n")
            for T_p, avg_current in zip(T_pList, averageCurrent):
                file.write(f"{T_p}, {avg_current}\n")

    if opg3d:
        print("Running opg3d")
        alphaList, averageCurrent = opg3dSim(N_p)
        with open('data\\results_opg3d.txt', 'w') as file:
            file.write("alphaList and averageCurrent:\n")
            for alpha, avg_current in zip(alphaList, averageCurrent):
                file.write(f"{alpha}, {avg_current}\n")
    
    if opg4b:
        print("Running opg4b")
        N_x = 10
        T_pList = np.linspace(80, 1500, 20).astype(int)
        averageCurrent = opg4bSim(N_p, N_x, T_pList)
        with open('data\\results_opg4b.txt', 'w') as file:
            file.write("T_pList and averageCurrent:\n")
            for T_p, avg_current in zip(T_pList, averageCurrent):
                file.write(f"{T_p}, {avg_current}\n")

    if opg4c:
        print("Running opg4c")
        betakList = [0.1, 1, 2, 3, 5, 10]
        for i, betak in enumerate(betakList):
            alphaList, averageCurrent = opg4cSim(N_p, betak)
            with open(f'data\\results_opg4c_betak_{i}.txt', 'w') as file:
                file.write("alphaList and averageCurrent:\n")
                for alpha, avg_current in zip(alphaList, averageCurrent):
                    file.write(f"{alpha}, {avg_current}\n")
        


def getData(choice=None):
    if choice == "opg3b":
        with open('data\\results_opg3b.txt', 'r') as file:
            lines = file.readlines()

            averageCurrent01 = []
            averageCurrent02 = []

            section = None
            for line in lines:
                line = line.strip()
                if line == "averageCurrent01:":
                    section = "averageCurrent01"
                elif line == "averageCurrent02:":
                    section = "averageCurrent02"
                elif section == "averageCurrent01" and line:
                    averageCurrent01.append(float(line))
                elif section == "averageCurrent02" and line:
                    averageCurrent02.append(float(line))
        return averageCurrent01, averageCurrent02

    elif choice == "opg3c":
        with open('data\\results_opg3c.txt', 'r') as file:
            lines = file.readlines()

            T_pList = []
            averageCurrent03 = []

            for line in lines:
                line = line.strip()
                if line and line != "T_pList and averageCurrent:":
                    T_p, avg_current = map(float, line.split(', '))
                    T_pList.append(T_p)
                    averageCurrent03.append(avg_current)
        return T_pList, averageCurrent03

    elif choice == "opg3d":
        with open('data\\results_opg3d.txt', 'r') as file:
            lines = file.readlines()

            alphaList = []
            averageCurrent = []

            for line in lines:
                line = line.strip()
                if line and line != "alphaList and averageCurrent:":
                    alpha, avg_current = map(float, line.split(', '))
                    alphaList.append(alpha)
                    averageCurrent.append(avg_current)
        return alphaList, averageCurrent

    elif choice == "opg4b":
        with open('data\\results_opg4b.txt', 'r') as file:
            lines = file.readlines()

            T_pList = []
            averageCurrent = []

            for line in lines:
                line = line.strip()
                if line and line != "T_pList and averageCurrent:":
                    T_p, avg_current = map(float, line.split(', '))
                    T_pList.append(T_p)
                    averageCurrent.append(avg_current)
        return T_pList, averageCurrent
    
    elif choice == "opg4c":
        
        betak_files = [f for f in os.listdir('data') if f.startswith('results_opg4c_betak_')]
        betakSimList = []
        for betak_file in betak_files:
            with open(os.path.join('data', betak_file), 'r') as file:
                lines = file.readlines()
                alphaList = []
                averageCurrent = []
                for line in lines:
                    line = line.strip()
                    if line and line != "alphaList and averageCurrent:":
                        alpha, avg_current = map(float, line.split(', '))
                        alphaList.append(alpha)
                        averageCurrent.append(avg_current)
                betakSimList.append(averageCurrent)

        return betakSimList
    
    else:
        print("Invalid choice")
        return None

# generateData(N_x * 1, opg3b=True)
# generateData(N_x * 1, opg3c=True)
# generateData(N_x * 1, opg3d=True)
# generateData(400, opg4b=True)
# generateData(N_x * 1, opg4c=True)

# Oppgave 3a
# ParticlesAbsPos = opg3aSim()
# for i, Pos in enumerate(ParticlesAbsPos): # plots each particles absolute position
#     AbsolutePosAxis = np.linspace(0, len(Pos[::400]), len(Pos[::400]))
#     plt.plot(AbsolutePosAxis, Pos[::400], markersize=1, label=f"Particle {i + 1}")

# plt.title("Absolute x position of particles")
# plt.xlabel(f"Cycles")
# plt.ylabel("Absolute x position")
# plt.legend()
# plt.show()

# Oppgave 3b
# averageCurrent01, averageCurrent02 = getData("opg3b")
# for i, val in enumerate(averageCurrent01):
#     print(f"cycle {i + 1}: {val:.2e}")

# for i, val in enumerate(averageCurrent02):
#     print(f"cycle {i + 1}: {val:.2e}")

#Oppgave 3c
# T_pList, averageCurrent03 = getData("opg3c")
# plt.plot(T_pList, averageCurrent03)
# plt.xlabel("T_p")
# plt.ylabel("Average Current")
# plt.title("Average Current vs T_p")
# plt.grid()
# plt.show()


#Oppgave 3d
# alphaList, averageCurrent04 = getData("opg3d")
# plt.plot(alphaList, averageCurrent04)
# plt.xlabel("Alpha")
# plt.ylabel("Average Current")
# plt.title("Average Current vs Alpha")
# plt.grid()
# plt.show()

# Oppgave 4a
# T_p = 500
# N_x = 100
# alphaList, averageCurrent04 = getData("opg3d")
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
# ax1.plot(alphaList, averageCurrent04, label="Simulated")
# ax1.plot(alphaList, [analyticalAverageCurrent(alpha, T_p, N_x) for alpha in alphaList], label="Analytical")
# ax1.set_xlabel("Alpha")
# ax1.set_ylabel("Average current")
# ax1.set_title("Average current over different Alpha")
# ax1.grid()
# ax1.legend()
# ax2.plot(alphaList, [abs(sim - ana) for sim, ana in zip(averageCurrent04, [analyticalAverageCurrent(alpha, T_p, N_x) for alpha in alphaList])])
# ax2.set_xlabel("Alpha")
# ax2.set_ylabel("Difference")
# ax2.set_title("Difference between Simulated and Analytical")

# plt.tight_layout()
# plt.show()

# Oppgave 4b
# alpha = 0.8
# N_x = 10
# T_pList, averageCurrent = getData("opg4b")
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
# ax1.plot(T_pList, averageCurrent, label="Simulated")
# ax1.plot(T_pList, [analyticalAverageCurrent(alpha, T_p, N_x) for T_p in T_pList], label="Analytical")
# ax1.set_xlabel("T_p")
# ax1.set_ylabel("Average current")
# ax1.set_title("Average current over different T_p")
# ax1.grid()
# ax1.legend()
# ax2.plot(T_pList, [abs(sim - ana) for sim, ana in zip(averageCurrent, [analyticalAverageCurrent(alpha, T_p, N_x) for T_p in T_pList])])
# ax2.set_xlabel("T_p")
# ax2.set_ylabel("Difference")
# ax2.set_title("Difference between Simulated and Analytical")
# ax2.grid()
# ax2.legend()

# plt.tight_layout()
# plt.show()


# Oppgave 4c
# T_p = 500
# N_x = 100
# alphaList = np.linspace(0, 1, 50)
# betakList = [0.1, 1, 2, 3, 5, 10]
# averageCurrents = getData("opg4c")
# print(averageCurrents)
# for i, averageCurrent in enumerate(averageCurrents):
    
#     plt.plot(alphaList, averageCurrent, label=f"Simulated with {betakList[i]}")
#     plt.plot(alphaList, [analyticalAverageCurrent(alpha, T_p, N_x) for alpha in alphaList], label="Analytical")
#     plt.xlabel("Alpha")
#     plt.ylabel("Average current")
#     plt.title(f"Average current over different Alpha with betak = {betakList[i]}")
#     plt.grid()
#     plt.legend()
#     plt.tight_layout()
#     plt.show()