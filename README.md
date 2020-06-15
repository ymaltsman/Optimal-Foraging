# Optimal-Foraging
This is part of a research project with Prof. Andrew Bernoff, Prof. Jasper Weinburd, and other undergraduate students for the Mathematics department at Harvey Mudd College, investigating optimal foraging in locust swarms.
<h3>Status Update for June 15th</h3>
<p>I found that up until recently, the contact variable would update according to the following mechanism: </p>
<pre><code> def gregupdate(self, time, row):
        """treats gregarization as an exponentially decaying function which 'jumps'
        whenever contact is made"""
        t = time
        T = locust.T
        K = locust.K
        self.contact=self.contact*np.exp(-t/T)
        self.contact += self.place.getlocusts()
        if self.phase == 0 and self.contact > K:
            self.phase = 1
        elif self.phase == 1 and self.contact < K/2:
            self.phase = 0
</code></pre>
<p>where the input "time" is the time since the start of the generation. What I replaced this with was:</p>
<pre><code>
def gregupdate(self, row):
        """treats gregarization as an exponentially decaying function which 'jumps'
        whenever contact is made"""
        T = locust.T
        K = locust.K
        self.contact=self.contact*np.exp(-1/T)
        self.contact += self.place.getlocusts()
        if self.phase == 0 and self.contact > K:
            self.phase = 1
        elif self.phase == 1 and self.contact < K/2:
            self.phase = 0
 </code></pre>
 <p>which ensures that the contact level decays from its most recent level, rather than jumping down to where it would be after 
 t time steps with no contact.</p>
 <p>I'm working on visualizing gregarization steady states as a function of the gregarization threshold K. Here are some images I've generated:</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/blob/master/imgs/numlocusts.png">
<p> Zooming in to the 40-50 range </p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/blob/master/imgs/findingthresh.png">
 
<h2>Background</h2>
<p> A striking characteristic of locusts is that when they are repeatedly stimulated by other locusts, they undergo a behavioural and physiological phase change in which they become gregarious. This gregarization is a neccessary component for destructive locust swarms to form, which can include millions of locusts flying in unison. </p>
<h2>Description</h2>
<p>In this package we aim to investigate marching locusts on a 2d grid. Initially, locusts are split between a control group that moves according to a random walk, and a gregarizing group that moves according to rules for either gregarious or solitary locusts. The population evolves based on whichever locusts have the best and worst foraging efficiencies. For a fuller illustration of the model, see the following <a href ="https://www.zenflowchart.com/docs/view/15wNJAPdRnVVdGyOXpZK">flowchart.</a></p>
<h2>Navigation</h2>
<p>The locust class in <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/locust.py">locust.py</a> contains the properties and methods for individual locusts, such as their rules for eating and moving. The gridpoint class in<a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/gridpoint.py"> gridpoint.py</a> contains the properties and methods for individual points that make up the 2d grid. These include the number of locusts and resources on a point, and rules for depletion and gain of resources. <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/simulate.py">simulate.py</a> contains a function dictating the simulation of the genetic algorithm itself, and contains parameters for the time period, size of the grid, and number and makeup of the locusts. Finally, <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/analysis.py">analysis.py</a> contains a few functions functions for testing and visualizing the results of the model.</p>
<h3> Installing from git source </h3>

```
git clone https://github.com/ymaltsman/optimal-foraging.git

```
