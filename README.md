# Optimal-Foraging
This is part of a research project with Prof. Andrew Bernoff, Prof. Jasper Weinburd, and other undergraduate students for the Mathematics department at Harvey Mudd College, investigating optimal foraging in locust swarms.

<h3>Status Update for 6th July</h3>
<p>It seems like very low thresholds are evolutionarily stable for both low resources and high resources.</p>
<p>I ran five simulations with only 10 resources. This is how the populations evolved after ten generations:</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/7_6run01.png">
<p>And after about 500 generations:</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/7_6run04.png">
<p>Similarly, five simulations with 100 resources. The first 25 generations:</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/hrun01.png">
<p>And after about 300 generations:</p>
<img src="https://github.com/ymaltsman/Optimal-Foraging/raw/master/imgs/hrun03.png">

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
