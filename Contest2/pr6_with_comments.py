"""PR 6"""
import numpy as np


def get_best_indices(ranks: np.ndarray, top: int, axis: int = 1) -> np.ndarray:
    """DEF"""
    arr_len = ranks.shape[axis]
    # print(arr_len)
    tmp_arr = np.argpartition(ranks, arr_len - top, axis=axis)
    # print(tmp_arr)
    tmp_val = np.partition(ranks, arr_len - top, axis=axis)
    # print(tmp_val)
    tmp_val = np.take(tmp_val, arr_len - top + np.arange(top), axis=axis)
    tmp_arr = np.take(tmp_arr, arr_len - top + np.arange(top), axis=axis)
    # print(np.argsort(-tmp_val, axis=axis))
    # tmp_arr[np.arange(tmp_arr.shape[0])] = tmp_arr[np.arange(tmp_arr.shape[0])[:, None], np.argsort(-tmp_val)]
    # val = plus_one()
    # tmp_arr[np.arange(arr_len)] = np.take(tmp_arr, [0, 1], axis=axis)
    tmp_arr = np.take_along_axis(tmp_arr, np.argsort(-tmp_val, axis=axis), axis=axis)
    # tmp_arr = np.take(tmp_arr, ret(), axis=0)
    # dists = np.rec.fromarrays([tmp_arr, tmp_val], names='x,y')
    # print(dists)
    # dists = dists[:, arr_len - top: arr_len]
    # tmp_arr = tmp_arr[:, arr_len - top: arr_len]
    # tmp_val = tmp_val[:, arr_len - top: arr_len]
    # print(tmp_val)
    # print(np.argsort(-tmp_val))
    # print(sorted(tmp_arr[0], key=lambda x: -ranks[0][x]))
    # print("%%%%%%")
    # print(np.arange(tmp_arr.shape[0])[:, None])
    # tmp_arr = tmp_arr[np.arange(tmp_arr.shape[0])[:, None], np.argsort(-tmp_val)]
    return tmp_arr


X = np.array([[16, 10, 3, 8, 14, 5, 6, 18, 4, 17, 12, 2, 19, 1, 0],
              [6, 4, 19, 15, 13, 11, 14, 0, 7, 18, 9, 12, 8, 17, 1],
              [9, 12, 1, 2, 11, 17, 19, 8, 13, 15, 16, 10, 0, 18, 7]])
arr_len1 = X.shape[1]
Y = np.take(X, arr_len1 - 5 + np.arange(5), axis=1)
# val = plus_one()
# print(next(val))
# print(next(val))
#print(Y)
# B = np.array([19, 10, 16, 15, 19, 1, 11, 18, 3, 1, 8])
# print(np.ravel(B))
# Dict = dict()
# print(sorted(B, key=lambda x: x % 2))
# print(np.sort(X, axis=1))
# print("!!!!")
# print(X[:, 0:2])
# print("-------")
print(get_best_indices(X, 2, 0))
# print(np.argpartition(B, 4))
# print(np.partition(B, 5))
