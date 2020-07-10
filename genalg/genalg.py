import numpy as np
import sys
sys.path.insert(1,"C:\\Users\\yoni\\optimal-foraging\\classes")
from fasterlocust import locust
from gridpoint import gridpoint
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import copy
np.random.seed(18)
import json
from scipy.spatial import distance
import math

def simulate(Ks =[], gens = 1, iters = 20000, drift=.1, width = 5, numrows = 1, rowlen = 100, R = 50, cutoff = 10, G = 30):
    """
    Parameters
    --------------------------------
    gens: number of generations
    iters: iterations per generations
    numrows x rowlen: dimensions of grid
    R: number of resources
    cutoff: the number of locusts that die off and are born each generation
    C, G: number of locusts in control and gregarizing groups, respectively
    genData: a boolean that dictates whether or not generational level data about the grid will be stored and returned

    Outputs
    ---------------------------------
    locusts: the list of locusts as instances of the locust class 
    grid: the 'grid' ie the list of gridpoints as instances of the gridpoint class
    props: a list that keeps track of the proportion of gregarizing locusts in 
    the population
    gridData: returns generational level grid data if set to true
    """

    locust.N=G
    locust.rowlen=rowlen
    gridpoint.R = R
    #set up grid
    grid = []
    for i in range(numrows):
        row = []
        for j in range(rowlen):
            point = gridpoint(j,0,0)
            row.append(point)
        grid.append(row)

    rlist=[]
    #distribute resources
    for i in range(len(grid)):
        for j in range(2):
            for r in range(R//2):
                x = (rowlen//4)+j*(rowlen//2)
                g = int(np.random.normal(x, width))%rowlen
                grid[i][g].gainfood()
                rlist.append(g)
    locust.rlist=rlist

    #now we'll make a 2d list of locusts    
    locusts=[]
    for i in range(numrows):
        locustr=[]
        for g in range(G):
            x = int(np.random.uniform()*len(grid[i]))
            if len(Ks) == 0:
                K=np.random.uniform()*50
            else:
                K=Ks[g]
            #x=rowlen//2
            placeg = grid[i][x]
            glocust=locust(placeg, 1, K)
            locustr.append(glocust)
            placeg.newlocust()
        locusts.append(locustr)
    locusts=np.array(locusts)
        

    #randomly reorder each list of locusts
    for r in range(len(locusts)):
        np.random.shuffle(locusts[r])

    #one of the things that we can measure is the proportion of gregarizing locusts
    props = []
    props.append(G/locust.N)
    
    
    #gridData will track the distribution of locusts and resources on the grid
    gridData = []
    locustData =[]
    for g in range(gens):
        greg=0
        cont=0
        gridr=[]
        locustr=[]
        gridr.append([x.resources for x in grid[0]])
        locustr.append([[l.K, l.getefficiency()] for l in locusts[0]])

        #run through a single gen
        for i in range(iters):
            gridr.append([x.resources for x in grid[0]])
            locustr.append([[l.K, l.getefficiency()] for l in locusts[0]])
            for r in range(len(locusts)):
                for l in range(len(locusts[r])):
                    locusts[r][l].iterate(locusts[r], i, grid[r])
        gridData.append(gridr)
        locustData.append(locustr)
        if gens > 1:
            for r in range(len(locusts)):
                
                #remove the worst performing locusts and replace them with the 'offspring' of the best locusts
                for n in range(cutoff):
                    min = locusts[r][2*n].getefficiency()
                    worst = locusts[r][2*n]
                    windex=2*n
                    for l in range(len(locusts[r])-(2*n)):
                        l=l+(2*n)
                        if locusts[r][l].getefficiency() < min:
                            min = locusts[r][l].getefficiency()
                            worst = copy.deepcopy(locusts[r][l])
                            windex=l
                    if windex != 2*n:
                        max = locusts[r][2*n].getefficiency()
                        best = locusts[r][2*n]
                        bindex=2*n
                    else:
                        max = locusts[r][(2*n)+1].getefficiency()
                        best = locusts[r][(2*n)+1]
                        bindex=(2*n)+1
                    for j in range(len(locusts[r])-(2*n)):
                        j=j+(2*n)
                        if locusts[r][j].getefficiency() > max and j != windex:
                            max = locusts[r][j].getefficiency()
                            best = copy.deepcopy(locusts[r][j])
                            bindex=j
                    worst.K = best.K
                    worst.phase=best.phase
                    worst.contact=best.contact
                    worst.consumed=best.consumed
                    worst.walked=best.walked
                    worst.getefficiency()
                    index=[bindex, windex]
                    tmp = copy.deepcopy(locusts[r])
                    tmp = np.delete(tmp, index)
                    tmp = np.insert(tmp,0,best)
                    tmp = np.insert(tmp,1,worst)
                    locusts[r]=copy.deepcopy(tmp)

                for loc in locusts[r]:
                    loc.reset(grid[r])
                
                for l in range(locust.N):
                    g=np.random.normal(locusts[r][l].K, locusts[r][l].K*drift)
                    if g <= 0:
                        g= 0.05
                    locusts[r][l].K = g
    distances=[]
    if gens > 1:
        for g in range(1,gens):
            a=[x[0] for x in locustData[g][iters-1]]
            b=[x[0] for x in locustData[g-1][iters-1]]
            d=distance.euclidean(a, b)
            d=math.ceil(d*100)/100
            distances.append(d)
        
        
    return [locusts, grid, props, gridData, locustData, distances]



def multplot(gens, iters, intervals, ran, load = 0, drift=.1):
    fig, axs = plt.subplots(intervals, ran)
    Ks=[]
    if load == 1:
        with open('genalgdata.txt', 'r') as filehandle:
            Ks=json.load(filehandle)
    klist=[]
    elist = []
    dlist = []
    for r in range(ran):
        width=10**r
        if len(Ks)>0:
            sim=simulate(Ks[r], gens=gens, iters=iters, width=width)
            o=sim[4]
            dlist.append(sim[5])
        else:
            sim=simulate(Ks, gens=gens, iters=iters, width=width)
            o=sim[4]
            dlist.append(sim[5])
        Kstr=[]
        effs = []
        ds = []
        for g in range(gens):
            if g % (gens/intervals) == 0:
                Ktemp=[x[0] for x in o[g][iters-1]]
                Kstr.append(Ktemp)
                #effs.append([x[1] for x in o[g][iters-1]])
        for i in range(intervals):
            axs[i][r].scatter(range(locust.N), Kstr[i])
            axs[i][r].set_ylabel("Threshold")
            axs[i][r].set_title(f"generation {i*(gens/intervals)}, width={10**r}")
        klist.append(Kstr[intervals-1])
    plt.setp(axs, ylim=(0,200))
    with open('genalgdata.txt', 'w') as filehandle:
        json.dump(klist, filehandle)
    fig.suptitle(f"Variation in simulations. {gens} generations, {iters} iterations each. Params: {locust.N} locusts, {gridpoint.R} resources, probability of {locust.p}, drift of {drift}")
    plt.show()


def singplot(gens, iters, intervals, load=0, drift=.05):
    fig, axs = plt.subplots(intervals, 2)
    Ks=[]
    Es=[]
    if load == 1:
        with open('singenalgdata.txt', 'r') as filehandle:
            Ks=json.load(filehandle)
    o=simulate(Ks, gens, iters, drift)[4]
    o=np.array(o)
    o = np.sort(o, axis=1)
    for g in range(gens):
        if g % (gens/intervals) == 0:
            Ks.append([x[0] for x in o[g][iters-1]])
            Es.append([x[1] for x in o[g][iters-1]])
    for i in range(intervals):
        axs[i][0].scatter(range(locust.N), Ks[i])
        axs[i][1].scatter(range(locust.N), Es[i])
        axs[i][0].set_ylabel(f"generation {(i+1)*(gens/intervals)}")
    newKs = Ks[intervals-1]
    with open('singenalgdata.txt', 'w') as filehandle:
        json.dump(newKs, filehandle)
    fig.suptitle(f"Change in threshold over {gens} generations, {iters} iterations each. Params: {locust.N} locusts, probability of {locust.p}")
    plt.show()

def showresources(width):
    o = simulate(gens=2,iters=1000, width=width)[3][1][999]
    print(sum(o))
    plt.scatter(range(locust.rowlen),o)
    plt.title(f"resource distribution with width of {width}")
    plt.ylim(0,30)
    plt.xlabel("location")
    plt.ylabel("resources")
    plt.show()


#function to run    
multplot(1000,2000,5,5,1)

