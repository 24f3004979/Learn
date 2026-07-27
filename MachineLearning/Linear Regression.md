Finding Linear pattern into the dataset.

Minimizing the error function which tells us how good the proposed structure function maps to the original dataset of our concern. 

Why taking square error ?
Easy differentiation, Moderate punishment for errors. takes distance structure due to distance formula structure.

Why Linear Regression ?
Taking function into higher dimension could lead variables to take the exact values from training dataset which leads to over-fitting of the model, resulting into testing phase.

Thus we would use constrained space of Linear Function to find pattern, which would ensure we don't over fit even if squared error comes to be zero.

## Geometric Interpretation of Linear Regression
Why do we have used psudo inverse into finding the Least square, I have previously learnt that we wont need such, What is really use of pseudo inverse and how its different from the original inverse thing ?

How we decide shape of  our target dataset, how we would take features and units ? 
In what basis would be assign things to take all features at once, or take features unit wise ?

## All Feature at once or with steps ?
**Taking all features at once gives the global situation with variability based on features structure at higher dimension, features if being independent then both ways would give same result**

Features loading at once is a choice of computational resources , but i am not able to find the exact difference with taking step by step, 
Since with matrix operations to understand things we take whole features set at once , and into optimized way we take with steps to understand the dataset.

Solution with respect to data points given in dataset, x vector comprises of all features packed unit, Its squared matrix might not be inverting due to which we took pseudo inverse and computed the final weights required for best fit for training dataset

Q : How does really this formula works into finding the best fit ?
	Q : What is really the formula finding ? :)  | Finding the weight for the model

$$
w^*=(xx^T)^+xy
$$
With respect to features vectors, Taking account of all features from the dataset, we can make a subspace where we can project the target vector to get the final solution,

Q: What we can interpret with projecting target vector into the subspace spanned by the feature vectors ? , How it is useful into regression problem ?


## Goodness of MLE for Linear Regression

Original Dataset could be result of given model where a underlying W is generating the dataset with some noise.
$$
prediction = W^T.X+{\eta}
$$

$$
\eta = N(\sigma,\omega)
$$
Final Expectation result
$$
E = [|{\hat W} - W|] => \sigma^2.tracce((XX^T)^+)
$$

## Probabilistic Skills are lacking for madhav to ace the exam as per the requirements set bby himself
Please study statistics in a good way and understand the underlying things about statistical models their modeling for the situations and get through those concepts correctly