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
