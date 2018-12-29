A random walk is a particular kind of probabilistic (pseudo-random) simulation that models certain statistical systems, such as Brownian motion of particles or molecules.  Coin flipping is an example of a one-dimensional random walk--one dimensional because you only can go forward (when you flip heads) or backward (when you flip tails) along a straight line.  Suppose you take a random walk of n steps.  How many steps away from your starting point would you expect to end up on average, if you repeated the experiment many times?

Now suppose we make it two-dimensional. Suppose you can go forward, backward, left and right. How many steps away from your starting point would you expect to end up on average, if you repeated this experiment many times?

And finally, suppose instead of just four choices, we could go any direction? We can generate a random direction using an angle from the x axis using equation 1.  Then we can use equations 2 and 3 to generate new positions for each time step.

(1) angle = random() * 2 * math.pi
(2) x = x + cos(angle)
(3) y = y + sin(angle)

Your program should take the number of steps as input. Assume the walker always starts at 0,0 in a 100x100 unit grid. Create a graphical program that will draw a line to trace the path of the walk as it progresses. At the end, print out the straight-line distance and actual distance traveled to the console or GUI, rounded to the nearest whole unit.  