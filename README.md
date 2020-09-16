# Optimal-Foraging
<h2>Background</h2>
<p> A striking characteristic of locusts is that when they are repeatedly stimulated by other locusts, they undergo a behavioural and physiological phase change in which they become gregarious. This gregarization is a neccessary component for destructive locust swarms to form, which can include millions of locusts flying in unison. </p>
<p>Over the course of summer 2020, I worked under the guidance of Prof. Andrew Bernoff and Prof. Jasper Weinburd of Harvey Mudd College to build a minimal model that could shed light into why, evolutionary, locusts find it advantageous to gregarize. I developed an agent based genetic algorithm as well as an ODE model to attempt to answer this question. I write about these models and their results in this <a href="https://drive.google.com/file/d/1MdATwdaKxNiT2bbB2fi1LEAmZ3JclstG/view">report</a>.
<h2>Agent Based Genetic Algorithm</h2>
<p>In <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/genalg.py">genalg.py</a> we investigate marching locusts on a 2d grid with varying propensities to gregarize (gregarization thresholds). The population evolves based on whichever locusts have the best and worst foraging efficiencies, potentially converging to a homogenous population. For a fuller illustration of the model, see the following <a href ="https://www.zenflowchart.com/docs/view/15wNJAPdRnVVdGyOXpZK">flowchart.</a></p>
<h2>ODE Model</h2>
In <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/ODEmodel.ipynb">ODEmodel.ipynb</a> we build up to a five dimensional system of ODEs that investigates the population dynamics of competing solitary locusts and gregarious locusts, as well as the resources that they consume. We borrow from the idea of producer-scrounger games in game theory. 
<h2>Navigation</h2>
<p>The locust class in <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/fasterlocust.py">fasterlocust.py</a> contains the properties and methods for individual locusts, such as their rules for eating and moving. The gridpoint class in<a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/classes/gridpoint.py"> gridpoint.py</a> contains the properties and methods for individual points that make up the 2d grid. These include the number of locusts and resources on a point, and rules for depletion and gain of resources. <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/genalg.py">genalg.py</a> contains a function dictating the simulation of the genetic algorithm itself, and contains parameters for the time period, size of the grid, and number and makeup of the locusts. <a href="https://github.com/ymaltsman/Optimal-Foraging/blob/master/bayesopt/bayesiansimulation.py">bayesiansimulation.py</a> runs a bayesian optimization on the model.</p>
<h3> Installing from git source </h3>

```
git clone https://github.com/ymaltsman/optimal-foraging.git

```
