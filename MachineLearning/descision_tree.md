# Decision Tree Algorithm
We seprate dataset  with border conditions, and make conditional driven clusters

## Approach
How to build the tree  🌳
> Pick feature which have largest information gain
    making a simple separation condition into the feature
    Then nest conditions for further separation
    making ultimate partition for the dataset

**Points to consider with building tree**
* Stopping condition
    When a node becomes pure stop there
    with probability of each class
    class1 > threshhold | higher chance for a class > Pure node

* Depth Problem 🍃
    If depth is too large then it would fit the noise also
    thus we take depth limit as hyper parameter.
    setup with validation set to guard rail depth

* Alternate Measure for good condition {question} : Gini index

### Blend of a question
with controlled way to allow to make depth fro the tree, we control the quality of model
If we would allow all required depth then data would get overfited
with some separating conditional questions we build the final tree for the dataset.
tree becomes pure at some point if its let with no limit to making the depth limit
One outlier would make the decision tree pure at every patch with overfiting venom

> cross validation : Used for making sure we stop with a depth due to validations with other subsets, 
making our model usefull | how we would be able to implement the validation thing ?

Q. How to implement the validation sequences and conditions{questions} for building the tree ?


### Why decision tree are top notch to exlpain its approach
Decision tree could explain with its conditions and questions which led to a decission for given question, with just ten questions deep dive into the classification reason it could be used to diagonise the situation, and give reason

could be used into implementing error tracing for students | needs clarity


