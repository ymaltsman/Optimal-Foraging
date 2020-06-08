import numpy as np
class locust:
    #biological parameters. r is sensing range, K is gregarization threshold, and T is a time constant
    r=1
    K=1
    T=10
    def __init__(self, place, group, phase = 0):
        """Each locust's state variables are location, amount of resources consumed, length walked, group (control = 0 or gregarizing = 1), phase (solitary=0 or gregarious = 1), 
        contact level, and orientation (1 or -1)
        """
        self.place=place
        self.location=place.location
        self.consumed=0
        self.walked=0.01
        self.group=group
        self.phase=phase
        self.contact=1
        self.efficiency = self.consumed/self.walked
        if np.random.uniform() < .5:
            self.sig = -1
        else:
            self.sig = 1

    def iterate(self, listoflocusts, time, row):
        if self.place.hasfood():
            self.eat(row)
        else:
            self.move(listoflocusts, time, row)
    
    def eat(self, row):
        self.consumed += 1
        self.place.losefood()
        #self.regenerate(row)


    def move(self, listoflocusts, time, row):
        """Updates location depending on the group and phase of the locust.
        For gregarizing, attracts/repels based on distance from other locusts
        """
        self.place.loselocust()
        if self.group == 0:
            v=np.random.uniform()
            if v < .5:
                self.location = (self.location - 1) % len(row)
            else:
                self.location = (self.location + 1) % len(row)
        else:
            self.gregupdate(time, row)
            a=0
            for i in range(len(listoflocusts)):
                d=abs(self.location - listoflocusts[i].location)
                if self.phase == 1:
                    a += listoflocusts[i].sig*np.exp(-d/(locust.r))
                else:
                    a += (-1)*listoflocusts[i].sig*np.exp(-d/locust.r)
            if a >= 0:
                self.sig=1
            else:
                self.sig=-1
            self.location = (self.location + self.sig) % len(row)
        self.place=row[self.location]
        self.walked += 1
        self.place.newlocust()
    
    def gregupdate(self, time, row):
        """treats gregarization as an exponentially decaying function which 'jumps'
        whenever contact is made"""
        t = time
        T = locust.T
        K = locust.K
        self.contact=np.exp(-t/T)
        self.contact += row[self.location].getlocusts()
        if self.phase == 0 and self.contact > K:
            self.phase = 1
        elif self.phase == 1 and self.contact < K/2:
            self.phase - 0

    def regenerate(self, row):
        x = int(np.random.uniform()*len(row))
        if row[x].hasfood() == False:
            self.regenerate(row)
        else:
            d = np.random.binomial(len(row),.5)
            if np.random.uniform() < .5:
                d = d*(-1) 
            m = (x+d) % len(row)
            row[m].gainfood()    
    
    




     
    
