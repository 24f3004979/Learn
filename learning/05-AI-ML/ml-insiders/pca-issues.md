# PCA Algorithm
Q: Why its used ?
    To reduce the elements requried for expressing given dataset
how the elements are reduced , what to do with those eigen values and eigen vectors into representing the dataset ? 

PCA : Dimentionality reduction part ? 
    Make a small activity with bare numbers about inner working of PCA and its requirements.

## Issues with PCA
1. Computation Issue
        Finding covariance matrix with the nXd matrix with too many feature comes to O(d^3) complexity making it hard for big feature dataset.
            Solution : Finding the eigen values and eigen vectors for the associative matrix X^TX matrix , but whats need for this way ?
            [task] : How really associative matrix is related to the X.XT based matrix, How we can find the eigen vectors with such ? of cross matrix types ?

2. Non-Linear Relationships
        Sometime the dataset directions importance cant the full picture

    Coking hypothesis
    How does the maping to higher dimension is making dataset playing linear into some sub space of that higher dimension ? 
    How does this is working to be having linear relation at higher dimension ? , HOW DO WE CAME UP WITH THE FORMULA FOR MAPING WITH SUCH DIMENSIONS ?

    Using combination pattern into maping features into higher dimentions with makinc choose thing from the given features, 

    Given 4 feature based dataset -> taking 3 out of thse we would have map target dimension with [ 1 4choose1, 4choose2 , 4choose3  ]
    Making multiple pairs of all possible feature combinations

