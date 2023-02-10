"""Program 4"""
import numpy as np


def get_max_after_zero(in_array):
    """Make nan every element before zero"""
    in_array = in_array.astype('float')
    find_zeros = np.where(in_array != 0)
    if in_array.size:
        in_array[0] = np.nan
    array2 = np.roll(in_array, -1, 0)
    array2[find_zeros[0]] = np.nan
    if np.all(np.isnan(array2)):
        return None
    max_val = max(array2[np.isnan(array2) == 0])
    return int(max_val)


# arr = np.array([1, 2, 0, 8, 0, 5])
# arr2 = np.split(arr, [1, 2])
# print(arr2)
A = np.array([[1, 2], [3, 4]])
X = np.array([0])
# X = X.astype('float')
# find_zeros = np.where(X != 0)
# print(np.array(find_zeros))
# print(find_zeros)
# print(find_zeros[0])
# Y = np.roll(X, -1, 0)
# Y[find_zeros[0]] = np.nan
# print(Y)
print(get_max_after_zero(X))
