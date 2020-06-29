<h3>Status Update for 29th June</h3>
<p>Last time we generated the following image, which gave us the idea that a low threshold wins out in the evolutionary algorithm.</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/convergence.png">
<p>However, doing five simulations (with the same initial conditions) seems to tell a more scattered story: </p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/scatter.png">
<p> There are a couple insights that we can look into further for this. In each simulation, the evolution at least converges to some range of threshold (25-30, 8-12, ~60, etc.)</p>
<p> I also looked into how the genetic algorithm evolves as a function of resources, which is inconclusive for now but might point in some interesting directions: </p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/databoy.png">
<p> In addition, I looked into whether increased performance with lower gregarization threshold might have to do with ballisticity instead, so I let both ballisticity and gregarization 
threshold be independant variables, and it seems like the population converges to lower ballisticity rather than lower threshold.</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/lowerball.png">
