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
 
