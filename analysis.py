import numpy as np
import random
from locust import locust
from gridpoint import gridpoint
from simulate import simulate
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

#what the grid looks like after resource distribution
def showresources():
    locusts, grid, props = simulate(0,0,1,100,50,0,0,0)
    dist = [x.resources for x in grid[0]]
    plt.scatter(range(len(grid[0])), dist)
    plt.show()

#proportion of gregarizing locusts over a number of simulations
def proplocusts(sims):
    listoflists=[]
    for i in range(sims):
        locusts, grid, props = simulate(20, 200)
        listoflists.append(props)
    for i in range(sims):
        plt.scatter(range(len(listoflists[i])),listoflists[i])
    plt.xlabel('generations')
    plt.ylabel('Gregarizing as portion of total')
    text = plt.text(-.5,.6, 'params \n gens: 20 \n iters: 200 \n grid: 1x100 \n Resources: 50 \n cutoff: 10', fontsize=8)
    text.set_path_effects([path_effects.Normal()])
    plt.show()
proplocusts(10)
