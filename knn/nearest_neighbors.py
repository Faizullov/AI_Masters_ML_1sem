import numpy as np
from knn.distances import euclidean_distance, cosine_distance


def get_best_ranks(ranks, top, axis=1, return_ranks=False):
    tmp_arr = np.argpartition(ranks, top, axis=1)
    tmp_val = np.partition(ranks, top, axis=1)
    tmp_val = np.take(tmp_val, np.arange(top), axis=1)
    tmp_arr = np.take(tmp_arr, np.arange(top), axis=1)
    tmp_arr = np.take_along_axis(tmp_arr, np.argsort(tmp_val, axis=1), axis=1)
    tmp_val = np.take_along_axis(tmp_val, np.argsort(tmp_val, axis=1), axis=1)
    if return_ranks:
        return tmp_val, tmp_arr
    return tmp_arr


class NearestNeighborsFinder:
    def __init__(self, n_neighbors, metric="euclidean"):
        self._X = None
        self.n_neighbors = n_neighbors
        if metric == "euclidean":
            self._metric_func = euclidean_distance
        elif metric == "cosine":
            self._metric_func = cosine_distance
        else:
            raise ValueError("Metric is not supported", metric)
        self.metric = metric

    def fit(self, X, y=None):
        self._X = X
        return self

    def kneighbors(self, X, return_distance=False):
        test = X
        matrix = self._metric_func(test, self._X)
        return get_best_ranks(matrix, self.n_neighbors, 1, return_distance)
