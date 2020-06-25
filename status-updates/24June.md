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
