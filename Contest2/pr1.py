"""Program 1"""
import numpy as np


def get_nonzero_diag_product(in_array):
    """def 1"""
    array = np.diagonal(in_array)
    if np.all(array == 0):
        return None
    total_prod = np.prod(list(filter(lambda y: y != 0, array)))
    return total_prod
