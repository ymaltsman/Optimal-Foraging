# Optimal-Foraging
This is part of a research project with Prof. Andrew Bernoff and Prof. Jasper Weinburd of the Mathematics department at Harvey Mudd College, investigating optimal foraging in locust swarms.
<h2>Background</h2>
<p> A striking characteristic of locusts is that when they are repeatedly stimulated by other locusts, they undergo a behavioural and physiological phase change in which they become gregarious. This gregarization is a neccessary component for destructive locust swarms to form, which can include millions of locusts flying in unison. </p>
<h2>Description</h2>
<p>In this package we aim to investigate marching locusts on a 2d grid. Initially, locusts are split between a control group that moves according to a random walk, and a gregarizing group that moves according to rules for either gregarious or solitary locusts. For a fuller illustration of the model, see the following <a href ="https://www.zenflowchart.com/docs/view/15wNJAPdRnVVdGyOXpZK">flowchart.</a></p>
<h2>Navigation</h2>
<p>The locust class in locust.py contains the properties and methods for individual locusts, such as their rules for eating and moving. The gridpoint class in gridpoint.py contains the properties and methods for individual points that make up the 2d grid. These include the number of locusts and resources on a point, and rules for depletion and gain of resources.</p>
