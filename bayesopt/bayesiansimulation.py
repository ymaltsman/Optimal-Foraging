<<<<<<< HEAD:bayesopt/bayesiansimulation.py
import numpy as np
import sys
print(sys.path)
sys.path.insert(1,"C:\\Users\\yoni\\optimal-foraging\\classes")
from fasterlocust import locust
from gridpoint import gridpoint
np.random.seed(18)

def simulate(K, gens = 1, iters = 20000, numrows = 1, rowlen = 100, R = 50, cutoff = 60, C = 0, G = 30, genData = False):
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

    locust.N=C+G
    locust.rowlen=rowlen
    gridpoint.R = R
    locust.K=K
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
        for c in range(C):
            x = int(np.random.uniform()*len(grid[i]))
            #x=rowlen//2
            placec = grid[i][x]
            clocust= locust(placec, 0)
            locustr.append(clocust)
            placec.newlocust()
        for g in range(C, C+G):
            x = int(np.random.uniform()*len(grid[i]))
            #x=rowlen//2
            placeg = grid[i][x]
            glocust=locust(placeg,1,K)
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
    
    
    locustData =[]
    for g in range(gens):
        locustr=[]
        
        #run through a single gen
        for i in range(iters):
            locustr.append([l.getefficiency() for l in locusts[0]])
            for r in range(len(locusts)):
                for l in range(len(locusts[r])):
                    locusts[r][l].iterate(locusts[r], i, grid[r])
        locustData.append(locustr)
    
    
    return np.average(locustData[0][iters-1])


from bayes_opt import BayesianOptimization
from bayes_opt.logger import JSONLogger
from bayes_opt.event import Events
from bayes_opt.util import load_logs


pbounds = {'K': (0, 100)}
optimizer = BayesianOptimization(
f=simulate,
pbounds=pbounds,
verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
random_state=1,
)

# New optimizer is loaded with previously seen points
load_logs(optimizer, logs=["./logs.json"])

logger = JSONLogger(path="./logs.json")
optimizer.subscribe(Events.OPTIMIZATION_STEP, logger)


optimizer.maximize(
init_points=5,
n_iter=10,
)




=======
import numpy as np
import random
from locust import locust
from gridpoint import gridpoint
def simulate(gens = 100, iters = 100, numrows = 1, rowlen = 100, R = 50, cutoff = 10, C = 30, G = 30, genData = False):
    """
    Parameters
    --------------------------------
    gens: number of generations
    iters: iterations per generations
    numrows x rowlen: dimensions of grid
    R: number of resources
    cutoff: the number of locusts that die off and are born each generation
    C, G: number of locusts in control and gregarizing groups, respectively
    genData: a boolean that dictates whether or not generational level data about the grid will be stored and returned -- not yet in use

    Outputs
    ---------------------------------
    locusts: the list of locusts as instances of the locust class 
    grid: the 'grid' ie the list of gridpoints as instances of the gridpoint class
    props: a list that keeps track of the proportion of gregarizing locusts in 
    the population
    gridData: returns generational level grid data if set to true
    locustData: returns generational level data about locusts
    """

    N=C+G

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
    locusts = []    
    for i in range(len(grid)):
        rowlocusts=[]
        for c in range(C):
            x = int(np.random.uniform()*len(grid[i]))
            place = grid[i][x]
            clocust = locust(place, 0)
            rowlocusts.append(clocust)
            clocust.place.newlocust()
        for g in range(G):
            x = int(np.random.uniform()*len(grid[i]))
            place = grid[i][x]
            glocust = locust(place, 1)
            rowlocusts.append(glocust)
            glocust.place.newlocust()
        locusts.append(rowlocusts)

    #randomly reorder each list of locusts
    for r in range(len(locusts)):
        random.shuffle(locusts[r])

    #one of the things that we can measure is the proportion of gregarizing locusts
    props = []
    props.append(G/N)
    
    #gridData will track the distribution of locusts and resources on the grid
    gridData = []
    locustData =[]
    print(sum([x.locusts for x in grid[0]]))
    for g in range(gens):
        greg=0
        cont=0
        gridr=[]
        locustr=[]
        
        #run through a single gen
        for i in range(iters):
            for r in range(len(locusts)):
                for l in range(len(locusts[r])):
                    locusts[r][l].iterate(locusts[r], i, grid[r])
            gridr.append([x.locusts for x in grid[0]])
            locustr.append([l.phase for l in locusts[0]])
        gridData.append(gridr)
        locustData.append(locustr)

        for r in range(len(locusts)):
            
            #remove the worst performing locusts
            for n in range(cutoff):
                min = locusts[r][0].efficiency
                worst = locusts[r][0]
                for l in range(len(locusts[r])):
                    if locusts[r][l].efficiency < min:
                        min = locusts[r][l].efficiency
                        worst = locusts[r][l]
                worst.place.loselocust()
                locusts[r].remove(worst)
            
            #best locusts reproduce
            for n in range(cutoff):
                max = locusts[r][0].efficiency
                best = locusts[r][0]
                for l in range(len(locusts[r])):
                    if locusts[r][l].efficiency > max:
                        max = locusts[r][l].efficiency
                        best = locusts[r][l]
                baby = locust(best.place, best.group, best.phase)
                locusts[r].append(baby)
                baby.place.newlocust()
        
        #updating proportion of gregarizing locusts
        for l in range(len(locusts[r])):
            if locusts[r][l].group == 0:
                cont += 1
            else:
                greg += 1
        props.append(greg/N)

    return [locusts, grid, props, gridData, locustData]








>>>>>>> 2ae708fa4a32a83ca52dd512e0d0cb627b435779:simulate.py
