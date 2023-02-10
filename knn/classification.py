import numpy as np

from sklearn.neighbors import NearestNeighbors
from knn.nearest_neighbors import NearestNeighborsFinder


class KNNClassifier:
    EPS = 1e-5

    def __init__(self, n_neighbors, algorithm='my_own', metric='euclidean', weights='uniform'):
        if algorithm == 'my_own':
            finder = NearestNeighborsFinder(n_neighbors=n_neighbors, metric=metric)
        elif algorithm in ('brute', 'ball_tree', 'kd_tree',):
            finder = NearestNeighbors(n_neighbors=n_neighbors, algorithm=algorithm, metric=metric)
        else:
            raise ValueError("Algorithm is not supported", metric)
        if weights not in ('uniform', 'distance'):
            raise ValueError("Weighted algorithm is not supported", weights)

        self._finder = finder
        self._weights = weights

    def fit(self, X, y=None):
        self._finder.fit(X)
        self._labels = np.asarray(y)
        return self

    def _predict_precomputed(self, indices, distances):
        if self._weights == 'uniform':
            labels = np.take(self._labels, indices)
            return np.array([np.bincount(i).argmax() for i in labels])
        labels = np.take(self._labels, indices)
        weight = np.ones(shape=(distances.shape[0], distances.shape[1])) / (distances + self.EPS)
        onehot = labels[..., None] == np.unique(self._labels)[None, None, :]
        tmp = weight[..., None] * onehot
        count = np.sum(tmp, axis=1)
        return np.argmax(count, axis=1)

    def kneighbors(self, X, return_distance=False):
        return self._finder.kneighbors(X, return_distance=return_distance)

    def predict(self, X):
        distances, indices = self.kneighbors(X, return_distance=True)
        return self._predict_precomputed(indices, distances)


class BatchedKNNClassifier(KNNClassifier):
    '''
    Нам нужен этот класс, потому что мы хотим поддержку обработки батчами
    в том числе для классов поиска соседей из sklearn
    '''

    def __init__(self, n_neighbors, algorithm='my_own', metric='euclidean', weights='uniform', batch_size=None):
        KNNClassifier.__init__(
            self,
            n_neighbors=n_neighbors,
            algorithm=algorithm,
            weights=weights,
            metric=metric,
        )
        self._batch_size = batch_size

    def set_batch_size(self, batch_size):
        self._batch_size = batch_size

    def kneighbors(self, X, return_distance=False):
        if self._batch_size is None or self._batch_size >= X.shape[0]:
            return super().kneighbors(X, return_distance=return_distance)
        sections = np.arange(0, len(X), step=self._batch_size) + self._batch_size
        array_of_split = np.split(X, sections.astype(int))
        counter_of_parts = int(np.ceil(len(X) / self._batch_size))
        distances, indices = super().kneighbors(array_of_split[0], return_distance=return_distance)
        res_ind = indices
        res_dist = distances
        for i in range(1, counter_of_parts):
            distances, indices = super().kneighbors(array_of_split[i], return_distance=return_distance)
            res_dist = np.vstack((res_dist, distances))
            res_ind = np.vstack((res_ind, indices))
        return res_dist, res_ind


