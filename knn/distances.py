import numpy as np


def euclidean_distance(X, Y):
    tmp = np.sum(np.power(X, 2), axis=1)
    tmp2 = np.sum(np.power(Y, 2), axis=1)
    tmp = tmp[:, np.newaxis]
    return np.sqrt(np.absolute((X @ Y.T)*(-2) + tmp + tmp2))


def cosine_distance(X, Y):
    Outer = np.ones(shape=(len(X), len(Y)))
    Matrix = X @ Y.T
    tmp = np.sum(np.power(X, 2), axis=1)
    tmp2 = np.sum(np.power(Y, 2), axis=1)
    Matrix = Matrix / np.sqrt(tmp)[:, np.newaxis]
    Matrix = Matrix / np.sqrt(tmp2)
    return Outer - Matrix
