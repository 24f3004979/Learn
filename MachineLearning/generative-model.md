# Generative Model Based Algorithm
Documented to explore the domain of generative modeling for dataset, Modeling aproaches and ways to improve for good models to warning represent the generation behind the dataset.

### GOAL PROBLEM : LEARN HOW DOES THE DATA IS GENERATED NOT JUST LABEL

**Naive Approach**
Assign initial conditional step, proceding with modeling all possibility with given subsets,
Modeling the generative side of dataset with exponential amount of parameters required to learn/estimate

**Parameters and Problem modeling**
Overview : Associating probability to posssibility after condition split with a probability
First Probability --> condition split --> individual event possibilities
    Q How we would assign probability to each of those events ?
    - required topics [pdf, cdf based approaches for defining mass probability systems] ~ modeling of situation into stats frame
    > Modeling thing with statistical approach | making probability assignment based on observation
    Making observation about the individual events distribution and modeling the situation with probability model

Total Parameter requirements : 2d + 1

**What we are loosing**
We are assuming that all possibilities are independent of each other, 
having one condition might link with other conditions probability but here we simply ignore those,

### CLASS CONDITIONAL INDEPENDENCE ASSUMPTION
Given a class, features are independent of each other
features occurence is independent of each other thus they dont have the relation they might have with link

Still this is profound model which works good

given features , f1, f2 ... fd are words probability given class | each words are independent of each other to occur
$$
p(x=[f1,f2,...f3]| y) = \prod_i^d (p_i)^f_i (1-p_i)^1-f_i
$$

how to estimate the parameters : Maximum Likelihood based methods to get parameters


