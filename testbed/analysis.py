import numpy as np
from fasterlocust import locust
from gridpoint import gridpoint
from fastersimulate import simulate
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numba import jit

np.random.seed(18)
#what the grid looks like after resource distribution
def showresources():
    locusts, grid, props, gridData, locustData = simulate(0,0)
    dist = [x.locusts for x in grid[0]]
    print(sum(dist))
    plt.scatter(range(len(grid[0])), dist)
    plt.show()
#showresources()

#proportion of gregarizing locusts over a number of simulations
def proplocusts(sims, gens=2, iters=10):
    fig, axs = plt.subplots(sims)
    for i in range(sims):
        locust.K=(i+1)*5
        props = simulate(gens, iters)[2]
        print(props)
        axs[i].scatter(range(gens+1),props)
        axs[i].set_title(f'Threshold: {locust.K}', wrap=True)
    fig.suptitle(f'y-axis: gregarizing as portion of total. gens: {gens}, iters: {iters}, grid: 1x100, Resources: 50, cutoff: 10', fontsize=10)
    plt.show()
#proplocusts(10,10,4000)

#checking resource distribution at certain time intervals
def resourcedensity(iters, intervals, resources = 50, N = 60):
    locusts, grid, props, gridData, locustData = simulate(1, iters, 1, 100, resources, 10, 0, int(N/2))
    fig, axs = plt.subplots(intervals)
    gridhist = []
    for i in range(iters):
        if i % (iters/intervals) == 0:
            gridhist.append(gridData[0][i])
    for j in range(intervals):
        axs[j].scatter(range(len(gridhist[j])),gridhist[j])
    for ax in axs.flat:
        ax.set(xlabel='location', ylabel='locusts')
    fig.suptitle(f'Evolution of locust density over {iters} iterations. ' + f'gens: 1, grid: 1x100, Resources: {resources}, locusts: {N/2}, gregarization threshold: {locust.K}',wrap =True)
    plt.show()

#resourcedensity(20000,10, 25,60)

#Seeing how phases of locusts change
def trackphase(iters, intervals, numrows=100, resources = 50, G= 30):
    o = simulate(1, iters, 1, numrows, 50, 10, 0, G)
    locustData= o[4]
    fig, axs = plt.subplots(intervals)
    locusthist = []
    for i in range(iters):
        if i % (iters/intervals) == 0 or i == 0:
            locusthist.append(locustData[0][i])
    for j in range(intervals):
        axs[j].scatter(range(len(locusthist[j])),locusthist[j])
    for ax in axs.flat:
        ax.set(xlabel='locust', ylabel='phase')
    fig.suptitle(f'Evolution of locust phase over {iters} iterations (WITHOUT resource regeneration). ' + f'gens: 1, iters: {iters}, grid: 1x{numrows}, Resources: {resources}, gregarizing locusts: {G}, gregarization threshold: {locust.K}',wrap =True)
    plt.show()

#trackphase(4, 4)

def singlelocust(iters):
    """tracking the location and contact level of a single locust over a generation
    """
    o = simulate(1, iters, 1, 100, 50, 10, 0, 30)
    locustData = o[4]
    billx = []
    billc =[]
    for i in range(iters):
        locustcont = [x[0] for x in locustData[0][i]]
        locustx = [x[5] for x in locustData[0][i]]
        billx.append(locustx[0])
        billc.append(locustcont[0])
    plt.scatter(range(iters), billx, c='r')
    plt.scatter(range(iters), billc, c='b')
    plt.xlabel(f'Time (seconds)')
    plt.ylabel(f'Contact level (orange), Location (blue)')
    plt.title(f'Trajectory of a single locust over {iters} iterations. Threshold: {locust.K}, {locust.N} locusts, {gridpoint.R} resources' )
    plt.show()

#singlelocust(20)

def multlocusts(iters, plots = 5):
    """tracking the location and contact level of multiple locusts over a generation
    """
    o = simulate(1, iters, 1, 100, 50, 10, 0, 2)
    fig, axs = plt.subplots(plots)
    for p in range(plots):
        locustData = o[4]
        billx = []
        billc =[]
        for i in range(iters):
            locustcont = [x[1] for x in locustData[0][i]]
            locustx = [x[0] for x in locustData[0][i]]
            billx.append(locustx[p])
            billc.append(locustcont[p])
        #axs[p].scatter(range(iters), billx)
        axs[p].scatter(range(iters), billc)
        #axs[p].set(ylabel=f'Contact level (orange), Location (blue)')
    plt.xlabel(f'Time (seconds)')
    fig.suptitle(f'Contact levels of {plots} locusts over {iters} iterations. y axis is location. Threshold: {locust.K}, {locust.N} locusts, {gridpoint.R} resources' )
    plt.show()

#multlocusts(15000, 2)

def lines(iters, locusts = 30):
    """tracking the location and contact level of multiple locusts over a generation
    """
    locust.p=.7
    locust.K=10
    o = simulate(1, iters, 1, 100, 50, 10, 0, locusts)
    for l in range(locusts):
        locustData = o[4]
        billx = []
        billc =[]
        for i in range(iters):
            #locustcont = [x[1] for x in locustData[0][i]]
            locustx = [x[0] for x in locustData[0][i]]
            billx.append(locustx[l])
            #billc.append(locustcont[p])
        plt.scatter(range(iters), billx)
        #axs[p].scatter(range(iters), billc)
        #axs[p].set(ylabel=f'Contact level (orange), Location (blue)')
    plt.xlabel(f'Time (seconds)')
    plt.ylabel('position')
    plt.title(f'Trajectory of {locusts} locusts over {iters} iterations. Threshold: {locust.K}, {locust.N} locusts, {gridpoint.R} resources, probability of {locust.p}' )
    plt.show()
#lines(500000, 30)

def meanvel(iters):
    o = simulate(1, iters, 1, 100, 50, 10, 0, 30)
    locustData = o[4]
    cons =[]
    walked = []
    eff = []
    for i in range(iters):
        toeff = np.average([x[4] for x in locustData[0][i]])
        eff.append(toeff)
        tocons= np.average([x[5] for x in locustData[0][i]])
        cons.append(tocons)
        towalk = np.average([x[6] for x in locustData[0][i]])
        walked.append(towalk)
    #plt.scatter(range(iters), cons, c='r')
    #plt.scatter(range(iters), walked, c='b')
    plt.scatter(range(iters), eff, c='g')
    plt.show()
#meanvel(5000)


def meanphase(iters, R=50, L=30):
    fig, axs = plt.subplots(2)
    locust.K=20
    o = simulate(1, iters, 1, 100, R, 10, 0, L)
    locustData = o[4]
    eff =[]
    greg=[]
    #point = [0, 0]
    for i in range(iters):
        avg = np.average([x[4] for x in locustData[0][i]])
        eff.append(avg)
        gregs = np.sum([x[3] for x in locustData[0][i]])
        greg.append(gregs)
        #if i >= 100 and point == [0,0] and phase[i] == phase[i-1]:
            #point = [i, phase[i]]
    axs[0].plot(range(iters), eff)
    plt.xlabel("Time (iterations)")
    axs[0].set_ylabel("Mean efficiency")
    axs[1].plot(range(iters), greg)
    axs[0].set_ylabel("Mean gregarization")
    fig.suptitle(f"Does mean foraging efficiency reach a steady state? Parameters: {iters} iterations, {R} resouces, {L} locusts on 1x100 grid, probability of {locust.p}, threshold of {locust.K}", wrap = True)
    plt.show()
meanphase(500000)


def comparemeanphase(iters, ran=10):
    ratios=[]
    avgs=[]

    for i in range(ran):
        R=10
        L=R*(i+1)
        o=simulate(1, iters, 1, 100, R, 10, 0, L)[4]
        phase=[]
        for j in range(iters):
            avg = np.sum([x[3] for x in o[0][i]])
            phase.append(avg)
        fullavg=np.average(phase)
        avgs.append(fullavg)
        ratios.append(R/L)

    for i in range(ran):
        L=60
        R=L*(i+1)//10
        o=simulate(1, iters, 1, 100, R, 10, 0, L)[4]
        phase=[]
        for j in range(iters):
            avg = np.sum([x[3] for x in o[0][i]])
            phase.append(avg)
        fullavg=np.average(phase)
        avgs.append(fullavg)
        ratios.append(R/L)
    plt.scatter(ratios,avgs)
    plt.xlabel("ratio of Resources to locusts")
    plt.ylabel("Average gregarization")
    plt.title(f"mean gregarization as a function of resources to locusts. {iters} iterations, 1x100 grid", wrap=True)
    plt.show()

#comparemeanphase(40000, 10)

def distfromorigin(iters, L=30, plots=10):
    fig, axs = plt.subplots(plots)
    for p in range(plots):
        locust.p=.7
        locust.T=(p+1)*1000
        locust.K=3
        o=simulate(1, iters, 1, 100, 50, 10, 0, L)[4]
        loc=[]
        phase=[]
        for i in range(iters):
            #avgl=np.average([np.absolute(x[0]-50) for x in o[0][i]])
            #loc.append(avgl)
            avgp=np.average([x[3] for x in o[0][i]])
            phase.append(avgp)
        axs[p].scatter(range(iters),phase)
        axs[p].set_title(f'Timescale = {locust.T}', wrap=True)
        #text= axs[p].text(4000, .05, f'Timescale: {locust.T} seconds \n Probability: {locust.p}', wrap=True)
        #text.set_path_effects([path_effects.Normal()])
        #text.set_path_effects([path_effects.Normal()])
    plt.xlabel("Time (seconds)")
    fig.suptitle(f"Change in gregarization based on timescale. 1x100 grid, 50 resources, {L} locusts, 'p' = {locust.p}", wrap=True)
    plt.show()
#distfromorigin(40000,30,7)

def meancontact(iters):
    o = simulate(1, iters, 1, 100, 50, 10, 0, 30)
    locustData = o[4]
    contact =[]
    for i in range(iters):
        avg = np.average([x[1] for x in locustData[0][i]])
        contact.append(avg)
    plt.scatter(range(iters), contact)
    plt.show()
#meancontact(1000)