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
    locusts, grid, props, gridData, locustData = simulate(0,10)
    dist = [x.resources for x in grid[0]]
    plt.scatter(range(len(grid[0])), dist)
    plt.show()
showresources()

#proportion of gregarizing locusts over a number of simulations
def proplocusts(sims):
    listoflists=[]
    for i in range(sims):
        locusts, grid, props, gridData, locustData = simulate(10, 10)
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
def resourcedensity(iters, intervals, resources = 50, N = 60):
    locusts, grid, props, gridData, locustData = simulate(1, iters, 1, 100, resources, 10, int(N/2), int(N/2))
    fig, axs = plt.subplots(intervals)
    gridhist = []
    for i in range(iters):
        if i % (iters/intervals) == 0:
            gridhist.append(gridData[0][i])
    for j in range(intervals):
        axs[j].scatter(range(len(gridhist[j])),gridhist[j])
    for ax in axs.flat:
        ax.set(xlabel='location', ylabel='locusts')
    fig.suptitle(f'Evolution of locust density over {iters} iterations (WITHOUT resource regeneration). ' + f'gens: 1, iters: {iters}, grid: 1x100, Resources: {resources}, locusts: {N}',wrap =True)
    plt.show()

#resourcedensity(100,5, 100)

#Seeing how phases of locusts change
def trackphase(iters, intervals, numrows=100, resources = 50, G= 30):
    o = simulate(1, iters, 1, numrows, 50, 10, 0, G)
    locustData= o[4]
    fig, axs = plt.subplots(intervals)
    locusthist = []
    for i in range(iters):
        if i % (iters/intervals) == 0:
            locusthist.append(locustData[0][i])
    for j in range(intervals):
        axs[j].scatter(range(len(locusthist[j])),locusthist[j])
    for ax in axs.flat:
        ax.set(xlabel='locust', ylabel='phase')
    fig.suptitle(f'Evolution of locust phase over {iters} iterations (WITHOUT resource regeneration). ' + f'gens: 1, iters: {iters}, grid: 1x{numrows}, Resources: {resources}, gregarizing locusts: {G}, gregarization threshold: {locust.K}',wrap =True)
    plt.show()

#trackphase(10000, 5, 1000)
