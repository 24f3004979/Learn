Origination : Computational considerations with linear regression core algorithm for w for making predictions

==Inverse computation time complexity==
$$
O(d^3)
$$

**Gradient Decent is an iterative process for finding the minimization of a function.**

Gradient Decent Algorithm core
$$
W^{t+1} = W^t -{\eta}^t.{\Delta}f(w^t)
$$
Q : What is the reasoning with gradient decent formula ?
Random guessed variables goes into gradient , with a scaled vector from gradient to move the direction into for finding minimum.

**Gradient Decent Algorithm** : If function consists of many local minima, then we cant insure gradient decent algorithm could find global minima,

Simple suggestion which might not scale up with big dataset
Possible Way : We can proceed with taking further targeting function from bigger scope to know about functions plots and project the function teleport with being low, thus we might be able to get the minima for any functions with gradient decent.


Q: What is the context about x and other variables used ? are they individual data points or list of all features together ? What really means to find solution with features vs finding solution with unit wise ?

### Stochastic gradient descent SGD
we would also implement this into multiple thread of pooling and try to make this communicate with threads to execute parallel into computing the final output :)
1. Take sample from dataset uniformly 
2. Find gradient Decent for those points 
3. Repeat for first batch for t times
4. Take average and move for next batch

We can make the computation easy with this batch processing unit for making the ML part | Exiting thing to implement the first real world ML unit would be made for yantragya library