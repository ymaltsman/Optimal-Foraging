# Optimal-Foraging
This is part of a research project with Prof. Andrew Bernoff, Prof. Jasper Weinburd, and other undergraduate students for the Mathematics department at Harvey Mudd College, investigating optimal foraging in locust swarms.

<h3> Status update for June 24th </h3>
<p> I've worked on optimizing K, the gregarization threshold, through Bayesian Optimization and a genetic algorithm. Bayesian Optimization over 52 values of
K yielded the following results, which seemed to indicate a) foraging efficiency is optimized for minimal values of K and b) foraging efficiency varies significantly for 
minimal values of K. </p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/blob/master/imgs/bayes1.png">
Note, however, that this optimization ran simulations of 20,000 iterations each. Foraging efficiency does not reach a steady state until much later, at least for a gregerization threshold
of 10. In this plot it seems as though foraging efficiency climbs after gregarization is reached, after which it eventually reaches a steady state. We also know that increasing the gregarization 
threshold makes the locusts take a longer time to gregarize, so we'd expect that they would reach their steady state efficiency later as well.
<img src="https://github.com/ymaltsman/Optimal-Foraging/blob/master/imgs/effpostgreg.png">
Initial results from the genetic algorithm seem to support that lower gregarization thresholds are favorable for foraging efficiency.
<img src="https://github.com/ymaltsman/Optimal-Foraging/blob/master/imgs/convergence.png">

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
