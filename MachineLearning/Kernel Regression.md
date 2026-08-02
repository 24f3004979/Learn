Map the regular linear regression expression to form a kernel to generalize for non-linear regression problem.

[task] : Make the Regression formula which is generalized for non-linear spaces for doing regression

With Kernel Regression, we project data points into infinite space, and get the exact relation of the points, 

We can control kernel regression with using ridge regression setup to prevent over-fit of the dataset, 
Kernel could also be used for the control of the ridge regression, 
$$
K(x,y) = exp(-||x-z||^2)/2 \sigma^2
$$

# Probabilistic View
Q How to do the Maximum likelihood thing for given dataset or even formulate , Model the problem to solve ?

[ task ] : Implement Maximum Likelihood utility for predicting parameters for given model to fit the dataset
	How to Approach for making such fit with making parameter estimations ?

*Conclusion* : **==Maximum Likelihood estimator assuming ZERO-MEAN gaussian noise is exactly same as Linear Regression with squared mean==**

If we choose squared error it also imply with natural distribution of error noise.

**==CHOOSING A NOISE SHOULD REFLECT WITH TAKING ERROR FUNCTION FOR THE MODEL==**

