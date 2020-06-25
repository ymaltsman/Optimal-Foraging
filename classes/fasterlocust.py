import numpy as np
np.random.seed(18)
class locust:
    #biological parameters. r is sensing range, K is gregarization threshold, and T is a time constant
    r=15
    #K=10
    T=60
    rowlen=100
    N=60
    #parameters for transition probabilities
    #S->M for high resources, low resources
    hsm=.0036
    lsm=.0045
    #M->S
    hms=.14
    lms=.02
    #exponents
    esm=.03
    ems=.005
    #probability of moving according to gregarization rules
    p=.6
    def __init__(self, place, group, K, B, phase = 0, contact=1, efficiency = 0):
        """Each locust's state variables are location, amount of resources consumed, length walked, group (control = 0 or gregarizing = 1), phase (solitary=0 or gregarious = 1), 
        contact level, and orientation (1 or -1)
        """
        self.place=place
        self.location=place.location
        self.consumed=0
        self.walked=0.01
        self.group=group
        self.phase=phase
        self.contact=contact
        self.efficiency = efficiency
        self.motion = np.random.binomial(1,.5)
        self.K=K
        self.B=B
        if np.random.uniform() < .5:
            self.sig = -1
        else:
            self.sig = 1

    def iterate(self, listoflocusts, time, row):
        self.pauseandgo(row)
        if self.motion == 0:
            self.sig=0
            if self.place.hasfood():
                self.eat(row)
        else:
            self.move(listoflocusts, time, row)

    def pauseandgo(self, row):
        R=self.place.resources
        if self.motion == 0:
           p= locust.hsm - (locust.hsm - locust.lsm)*np.exp(-locust.esm*R)
           self.motion = np.random.binomial(1,p)
        else:
            p= locust.hms - (locust.hms - locust.lms)*np.exp(-locust.ems*R)
            self.motion = np.random.binomial(1,p)


    
    def eat(self, row):
        self.consumed += 1
        self.place.losefood()
        self.regenerate(row, self.place)
        self.sig=0


    def move(self, listoflocusts, time, row):
        """Updates location depending on the group and phase of the locust.
        For gregarizing, attracts/repels based on distance from other locusts
        """
        self.place.loselocust()
        if self.group == 1:
            self.gregupdate(time, row)
        if self.group == 0 or self.phase == 0:
            v=np.random.uniform()
            if v < self.B:
                self.location = (self.location - 1) % locust.rowlen
            else:
                self.location = (self.location + 1) % locust.rowlen
        else:
            if np.random.binomial(1,locust.p) == 1:
                a=0
                xlist = np.exp((-1/locust.r)*np.absolute(np.array([x.location for x in listoflocusts])-np.full((1,locust.N),self.location)))
                a = np.sum(xlist)
                if a >= 0:
                    self.sig=1
                else:
                    self.sig=-1
            else:
                self.sig=-1+2*(np.random.binomial(1,.5))
            self.location = (self.location + self.sig) % locust.rowlen
        self.place=row[self.location]
        self.walked += 1
        self.place.newlocust()
    
    def gregupdate(self, time, row):
        """treats gregarization as an exponentially decaying function which 'jumps'
        whenever contact is made"""
        #t = time
        T = locust.T
        K = self.K
        self.contact=self.contact*np.exp(-1/T)
        self.contact += self.place.getlocusts()
        if self.phase == 0 and self.contact > K:
            self.phase = 1
        elif self.phase == 1 and self.contact < K/2:
            self.phase = 0

    def regenerate(self, row, place):
        x = int(np.random.uniform()*100)
        i=0
        while i < 15 and place.hasfood() == False:
            x = x**2 % 100
            i += 1
        d = np.random.binomial(100,.5)
        if np.random.uniform() < .5:
            d = d*(-1) 
        m = (x+d) % 100
        row[m].gainfood()    

    def getefficiency(self):
        self.efficiency=(self.consumed)/np.sqrt(self.walked)
        return self.efficiency
    
    def reset(self, row):
        self.place.loselocust()
        x=int(np.random.uniform()*len(row))
        self.place=row[x]
        self.location=x
        self.place.newlocust()
        self.consumed=0
        self.walked=0.01
        self.contact=1
        self.motion = np.random.binomial(1,.5)
        self.getefficiency()
    




     
    
