# PACKAGE: DO NOT EDIT
# import inline
import numpy as np
import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.style.use('fivethirtyeight')
# from sklearn.datasets import fetch_olivetti_faces
# import time
# import timeit
# # %matplotlib inline


def mean(X):
    """Compute the sample mean for a dataset.

    Args:
        X: `ndarray` of shape (N, D) representing the dataset.
        N is the size of the dataset (the number of data points)
        and D is the dimensionality of each data point.
        ndarray: ndarray with shape (D,), the sample mean of the dataset `X`.
    """
    # YOUR CODE HERE
    ### Uncomment and edit the code below
    N, D = X.shape
    m = np.zeros((D,))
    for d in range(D):
        m[d] = np.sum(X[:, d]) / N

    return m

if __name__ == '__main__':
    X_1 = np.array([[0., 1., 1.],
                  [1., 2., 1.]])
    expected_mean_1 = np.array([0.5, 1.5, 1.])
    X_2 = np.array([[0., 1., 0.],
                  [2., 3., 1.]])
    expected_mean_2 = np.array([1., 2., 0.5])
    test_1 = mean(X_1)
    test_2 = mean(X_2)
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_mean_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_mean_2}")

