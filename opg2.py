import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from lib import Particle

# Oppgave 2a

def calculation(V, name):
    betakList = [0.01, 1, 100]
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))

    for i, betak in enumerate(betakList):
        Particles = [Particle(V, betak) for _ in range(numberOfParticles)]
        for j, _ in enumerate(range(numberOfSteps)):
            print(f'Step: {j} with beta*k = {betak}')
            for particle in Particles:
                particle.walkStep()

        positions = np.array([particle.getPos() for particle in Particles])
        mu, sigma = stats.norm.fit(positions)
        x = np.linspace(min(positions), max(positions), 1000)
        pdf = stats.norm.pdf(x, mu, sigma)
        ax[i].plot(x, pdf, 'r-', label=f"μ={mu:.2f}, σ={sigma:.2f}, βk {betak}")
        ax[i].hist(positions, bins=20, density=True, alpha=0.6, color='g')
        ax[i].set_title(f"βk = {betak}")
        ax[i].set_xlabel("Position")
        ax[i].set_ylabel("Probability density")
        ax[i].legend()

    fig.suptitle(f"Particle distribution with potetial {name}")
    plt.show()

# numberOfParticles = 10_000
# numberOfSteps = 200
numberOfParticles = 1_000 # 10 000 etter oppgave 2
numberOfSteps = 50

V = {'k' : lambda x: 1,
     '-k*x' : lambda x: -x, 
     'k(x/15 - np.cos(x/3))' : lambda x: x/15 - np.cos(x/3), 
     'k*x**4' : lambda x: x**4}

# calculation(V['k'], "k")
# calculation(V['-k*x'], "-k*x")
# calculation(V['k(x/15 - np.cos(x/3))'], 'k(x/15 - np.cos(x/3))')
# calculation(V['k*x**4'], 'k*x**4')

# test = Particle(V['-k*x'], 1)
# for _ in range(10):
#     test.walkStep()
#     print(f"pos: {test.getPos()} prob(-,0,+):{test.getProb()}")

