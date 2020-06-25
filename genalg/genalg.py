import numpy as np
import sys
sys.path.insert(1,"C:\\Users\\yoni\\optimal-foraging\\classes")
from fasterlocust import locust
from gridpoint import gridpoint
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import copy
np.random.seed(18)

def simulate(gens = 1, iters = 20000, drift=.1, numrows = 1, rowlen = 100, R = 50, cutoff = 10, G = 30, genData = False):
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

    #distribute resources
    for i in range(len(grid)):
        for r in range(R):
            x = int(np.random.uniform()*rowlen)
            grid[i][x].gainfood()


    #redistribute the resources to have a more realistic distribution. Resources are placed near other resources
    setuptime = 1000
    for i in range(len(grid)):
        for t in range(setuptime):
            x = int(np.random.uniform()*rowlen)
            if grid[i][x].hasfood():
                grid[i][x].losefood()
                y = int(np.random.uniform()*rowlen)
                if grid[i][y].hasfood():
                    d = np.random.binomial(rowlen,.5)
                    if np.random.uniform() < .5:
                        d = d*(-1) 
                    m = (y+d) % rowlen
                    grid[i][m].gainfood() 
                else:
                    grid[i][x].gainfood()

    #note - should figure out some kind of clumpiness measure at some point

    #now we'll make a 2d list of locusts    
    locusts=[]
    for i in range(numrows):
        locustr=[]
        for g in range(G):
            x = int(np.random.uniform()*len(grid[i]))
            K=int(np.random.uniform()*50)
            B=np.random.uniform()*.5
            #x=rowlen//2
            placeg = grid[i][x]
            glocust=locust(placeg, 1, K, B)
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
        
        #run through a single gen
        for i in range(iters):
            gridr.append([x.locusts for x in grid[0]])
            locustr.append([[l.K, l.B] for l in locusts[0]])
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
                    max = locusts[r][2*n].getefficiency()
                    best = locusts[r][2*n]
                    bindex=2*n
                    for j in range(len(locusts[r])-(2*n)):
                        j=j+(2*n)
                        if locusts[r][j].getefficiency() > max:
                            max = locusts[r][j].getefficiency()
                            best = copy.deepcopy(locusts[r][j])
                            bindex=j
                    worst.K = best.K
                    worst.B = best.B
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

                N = int(np.random.uniform()*locust.N)
                for l in range(N,N+5):
                    if l >= locust.N:
                        l = l % locust.N
                    d=-1+2*(np.random.binomial(1,.5))
                    locusts[r][l].K += locusts[r][l].K*drift*d
            
        
        

    return [locusts, grid, props, gridData, locustData]

def plot(gens, iters, intervals, drift=.1):
    o=simulate(gens, iters)[4]
    fig, axs = plt.subplots(intervals)
    Ks=[]
    Bs=[]
    for g in range(gens):
        if g % (gens/intervals) == 0:
            Ks.append([x[0] for x in o[g][iters-1]])
            Bs.append([x[1] for x in o[g][iters-1]])
    for i in range(intervals):
        axs[i].scatter(Ks[i], Bs[i])
        axs[i].set_ylabel("Ballisticity")
        plt.xlabel("Threshold")
    fig.suptitle(f"Changes in gregarization threshold and ballisticy over {gens} generations, {iters} iterations each. Params: {gridpoint.R} resources, {locust.N} locusts, probability of {locust.p}")
    plt.show()

plot(50,20000, 10)
