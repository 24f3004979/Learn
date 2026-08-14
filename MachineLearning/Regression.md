# Linear Regression [ Least Squares ]

Optimal weights with matrix way, to get the optimal fit

$$
w^* = (XX^T)Xy
$$

## Graphical view and inituation

Target vector is projected into feature space, projecting target vector into the feature space.
+ Implementation doubts
    - how to create the feature space what its really
    - visualization of projection
    - how to map the raw dataset into visualization flow with target vector

- How really the X.X^T and X.T.X could be made sense with ?
**How we can expand this idea into seeing things with more data points and create space  and projection**

How we can justify the fact that X.Tw* makes projection of lable vector into the feature space.

[info: Required visualization for this part about how does really the projection works]

# Gradient Descent
Heading towards minimizing function through going into opposite direction of the error function, with a learning rate and starting variable.

+ Gradient Descent [ One data iteration ]
    iterating all data points at once with complexity O(d^2)
+ Batch based
    Iterating weights after each batch

## Probabilistic view of linear regression
With initial synthetic dataset with random distribution

we can study the samples to predict the ultimate model and parameter with expectation fo the w hat ML estimations
Making assumption with dataset -> predicting the final weights without dataset

With Maximum Likelihood estimation problem we are trying to find the best parameter estimation for given dataset, we take expectation for geting the exact w value, since Maximum Likelihood Function shows the distribution of the weight being made out of the condition of radnomized generation form the noice based linear model

- Implement k fold based method the validation pipeline for the given set of problems
- Find out of activity of finding hyper parameter

## Bayesian Estimation
prior and posterior based framework for finding the parameters
How does this thing works ? What is the thing which makes sense with this approach ? 
How to implement this into working implementation ?

Multivariate distribution based approach for these such problems | We need to have good statistical understanding about those core operations

Ridge regression module with having contrained optimization problem for overcomming overfit
    Implementation is must required paired with derivation for the given expressions for the optimization
posterior  is proportional to Likelihood X Prior distribution
