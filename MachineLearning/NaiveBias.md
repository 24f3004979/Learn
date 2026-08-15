# Bayese Approach | Parameter estimation
Assumed model, with a first model deciding two ways, with sub independent probabilities.
We would approach with maximum Likelihood based estimation for bernouli parameters.

==*Simle parater assignment with most logical approach*==
First conditional step paramter maximum estimate = Fraction of that event
simple initiation of probability with fraction from given dataset

For features = fraction of given feature occured in total class element
among a class how many times this perticular feature occured.

Exp : Can we make a generator with given modeling of words through given set of dataset ?
    There we would need to make nested probability dependency 


### Prediction
given test word : ${0,1}^d$

Probability to find label of the given element given its features
which class have high probability with given dataset | simple cmparision based

features would be from our words set, they all are given probability
    simply multiplying the setup of probability would give us the final computed probability with given word

**Bayse Rule Approach for finding probability**
Finding probability of given test label of a specific class
Equals
probability of geting such feature combination ~ multiplying all probability of given feature sets
geting such features given target class chained probabilityt 

$$
p(y^{test}=1 | x^{test}) = \frac{p(x^{test} | y^{test}=1).p(y^{test}=1)}{p(x^{test})}
$$


