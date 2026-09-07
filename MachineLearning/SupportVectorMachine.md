# Breif Mention : Perceptrone Algorithm

Classification algorithm for finding weights such that it classifies the given dataset
works with given constraints to the dataset

**Constraints**
1. Defined upper cap to the dataset
2. Linear Separability
3. Margin

## Proof of working

$gama$ is the margin separation for the dataset

$$
mistakes = \frac{R^2}{\gamma}
$$

## Problems

> Finds the weight which separates the dataset

We also want the one which can maximize the total width of the decission boundary for given dataset to make the weight generalized for unseen dataset, Thus we need ways to maximize the width

## Solution

SVM : Support Vector machine

with formulating dual problem withh 2 constraint problem of **width minimization** along with alpha maximization for lagrange multiplier, 
we get to know about the complementry slackness situation

**which conveys only for truely contributing points out of given dataset effects the core weight vector for separation**

We can compress billions of data points with these few points for separation, along with use kernalization with thse few points for complex big dataset convey with small storage for weigths trained due to supporting vector importance.
🪃

$$
w^* = XY \alpha
$$

--- 

## Real World contains problems a lot of them 🐈‍⬛

1. Soft Margin approachh

Making every w feasible :) with bribe paying points which gets miss classified
Formula modification , 

editing same condition with svm with one margin containing one bribe variable
One more varible to minimize which is e {bribe condition to minimize}
we want to minimize the bribe payment for the given condition

*Problem with this formulation*
We allow all weights with the help of bribe condition to be a valid weight element
along with allowing big set of weights to join the group

Make panalty for paying bribe minimization expression gets addition with sum of all bribes to be minimized with length of weight
> with panalty with bribes now we would head towards good direction with balancing factor C <-- Hyper parameter

Final Modiefied Formulation for the Soft Margin SVM

**CONDITION 1**

Minimize $w$ along with $\xi_i$ with Hyper parameter $C$
$$

\frac{1}{2} ||w||^2 + C \sum_{i=1}^n \xi_i

$$

with modified expression of bribe based soft margin

$$

(w^Tx_i)y_i + \xi_i >= 1

$$
