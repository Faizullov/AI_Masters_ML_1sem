from collections import defaultdict

import numpy as np

from sklearn.model_selection import KFold, BaseCrossValidator
from sklearn.metrics import accuracy_score

from knn.classification import BatchedKNNClassifier


def knn_cross_val_score(X, y, k_list, scoring, cv=None, **kwargs):
    y = np.asarray(y)
    if scoring == "accuracy":
        scorer = accuracy_score
    else:
        raise ValueError("Unknown scoring metric", scoring)
    if cv is None:
        cv = KFold(n_splits=5)
    elif not isinstance(cv, BaseCrossValidator):
        raise TypeError("cv should be BaseCrossValidator instance", type(cv))
    k_to_scorer = {}
    kwargs['n_neighbors'] = max(k_list)
    how_class = BatchedKNNClassifier(**kwargs)
    for i in k_list:
        k_to_scorer[i] = np.empty(0)
    for train, test in cv.split(X):
        how_class.fit(X[train], y[train])
        dist, ind = how_class.kneighbors(X[test], return_distance=True)
        for i in k_list:
            tmp_dist = dist[:, 0:i]
            tmp_ind = ind[:, 0:i]
            k_to_scorer[i] = np.append(k_to_scorer[i], scorer(how_class._predict_precomputed(tmp_ind, tmp_dist), y[test]))
    return k_to_scorer

