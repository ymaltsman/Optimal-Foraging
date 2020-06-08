import numpy as np
import random
from locust import locust
from gridpoint import gridpoint
from simulate import simulate
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

np.random.seed(18)
#what the grid looks like after resource distribution
def showresources():
    locusts, grid, props, gridData = simulate(1,10)
    dist = [x.resources for x in grid[0]]
    plt.scatter(range(len(grid[0])), dist)
    plt.show()
#showresources()

#proportion of gregarizing locusts over a number of simulations
def proplocusts(sims):
    listoflists=[]
    for i in range(sims):
        locusts, grid, props, gridData = simulate(10, 10)
        listoflists.append(props)
    for i in range(sims):
        plt.scatter(range(len(listoflists[i])),listoflists[i])
    plt.xlabel('generations')
    plt.ylabel('Gregarizing as portion of total')
    text = plt.text(-.5,.7, 'params \n gens: 20 \n iters: 200 \n grid: 1x100 \n Resources: 50 \n cutoff: 10', fontsize=10)
    text.set_path_effects([path_effects.Normal()])
    plt.show()
#proplocusts(10)

#checking resource distribution at certain time intervals
def resourcedensity(iters, intervals):
    locusts, grid, props, gridData = simulate(1, iters)
    fig, axs = plt.subplots(5)
    gridhist = []
    for i in range(iters):
        if i % (iters/intervals) == 0:
            gridhist.append(gridData[0][i])
    for j in range(intervals):
        axs[j].scatter(range(len(gridhist[j])),gridhist[j])
    for ax in axs.flat:
        ax.set(xlabel='location', ylabel='resources')
    fig.suptitle('Evolution of resource distribution over {} iterations (with resource regeneration)'.format(iters))
    plt.show()

#resourcedensity(200,5)
