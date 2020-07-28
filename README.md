# Optimal-Foraging
We find what seem to be bifurcations in the dynamics of the system as gamma and k are adjusted.
We see in this image that gregarious locusts outperform solitary ones.
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/kprebifurcation.jpg">
When we increase k by .01, this switches pretty drastically:
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/kpostbifurcation.jpg">
As we increase gamma, we would expect gregarious locusts to perform better, but instead the discrepency increases in favor of solitary locusts, with both groups' populations lower.
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/highergammabiggerchange.png">
We increase gamma and the discrepancy increases even more.
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/gammaprebifurcation.jpg">
BUT, there appears to be another bifurcation when we increases gamma by .01:
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/gammapostbif.jpg">
And then if we decrease k by a bit, the discrepency switches in favor of gregarious locusts:
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/lowkgregwins.jpg">
<h2>Background</h2>
<p> A striking characteristic of locusts is that when they are repeatedly stimulated by other locusts, they undergo a behavioural and physiological phase change in which they become gregarious. This gregarization is a neccessary component for destructive locust swarms to form, which can include millions of locusts flying in unison. </p>
<h2>Description</h2>
<p>In this package we aim to investigate marching locusts on a 2d grid. Initially, locusts are split between a control group that moves according to a random walk, and a gregarizing group that moves according to rules for either gregarious or solitary locusts. The population evolves based on whichever locusts have the best and worst foraging efficiencies. For a fuller illustration of the model, see the following <a href ="https://www.zenflowchart.com/docs/view/15wNJAPdRnVVdGyOXpZK">flowchart.</a></p>
<h2>Navigation</h2>
<p>The locust class in <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/fasterlocust.py">fasterlocust.py</a> contains the properties and methods for individual locusts, such as their rules for eating and moving. The gridpoint class in<a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/gridpoint.py"> gridpoint.py</a> contains the properties and methods for individual points that make up the 2d grid. These include the number of locusts and resources on a point, and rules for depletion and gain of resources. <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/genalg/genalg.py">genalg.py</a> contains a function dictating the simulation of the genetic algorithm itself, and contains parameters for the time period, size of the grid, and number and makeup of the locusts. <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/bayesopt/bayesiansimulation.py">bayesiansimulation.py</a> runs a bayesian optimization on the model</p>
<h3> Installing from git source </h3>

```
git clone https://github.com/ymaltsman/optimal-foraging.git

```
