"""Program 3"""
import numpy as np


def replace_nan_to_means(in_array):
    """DEF"""
    columns = np.nanmean(in_array, axis=0)
    find_nans = np.where(np.isnan(in_array))
    in_array[find_nans] = np.take(columns, find_nans[1])
    return in_array



X = np.array([[4, 1, 3], [np.nan, 1, np.nan], [5, np.nan, 7]])
print(replace_nan_to_means(X))
# arr = np.delete(X, np.where(np.isnan(X)))
# print(arr)
# print("---")
# changed = X[np.isnan(X) == 0]
# print(changed)
# print(np.argwhere(np.isnan(X)))
# Y = np.ma.masked_equal(X, 1)
# print(Y)
# print(np.mean(Y, axis=0))
# if np.all(X == np.nan):
#     print("NAN!!!")
# print(np.mean(X, axis=0))
