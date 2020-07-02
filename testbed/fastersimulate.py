import numpy as np
import sys
sys.path.insert(1,"C:\\Users\\yoni\\optimal-foraging\\classes")
from fasterlocust import locust
from gridpoint import gridpoint
np.random.seed(18)

def simulate(gens = 1, iters = 20000, numrows = 1, rowlen = 100, R = 50, cutoff = 60, C = 0, G = 30, genData = False):
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
            glocust=locust(placeg,1)
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
            locustr.append([[l.location, l.contact, l.sig, l.phase, l.getefficiency(), l.consumed, l.walked, l.group] for l in locusts[0]])
            for r in range(len(locusts)):
                for l in range(len(locusts[r])):
                    locusts[r][l].iterate(locusts[r], i, grid[r])
        gridData.append(gridr)
        locustData.append(locustr)
        if gens > 1:
            for r in range(len(locusts)):
                
                #remove the worst performing locusts and replace them with the 'offspring' of the best locusts
                for n in range(cutoff):
                    min = locusts[r][0].getefficiency()
                    worst = locusts[r][0]
                    for l in range(len(locusts[r])):
                        if locusts[r][l].getefficiency() < min:
                            min = locusts[r][l].getefficiency()
                            worst = locusts[r][l]
                    max = locusts[r][0].getefficiency()
                    best = locusts[r][0]
                    for l in range(len(locusts[r])):
                        if locusts[r][l].getefficiency() > max:
                            max = locusts[r][l].getefficiency()
                            best = locusts[r][l]
                    worst.group = best.group
                    worst.phase=best.phase
                    worst.contact=best.contact
                    worst.efficiency=best.getefficiency()

                for loc in locusts[r]:
                    loc.reset(grid[r])

        
            
            #updating proportion of gregarizing locusts
        for r in range(len(locusts)):
            for l in range(len(locusts[r])):
                if locusts[r][l].group == 0:
                    cont += 1
                else:
                    greg += 1
        props.append(greg/locust.N)
        

    return [locusts, grid, props, gridData, locustData]









