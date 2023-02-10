"""Program 5"""
import numpy as np


def encode_rle(in_array):
    """DEF"""
    start_def = np.ones(len(in_array))
    np.not_equal(in_array[1:], in_array[:-1], out=start_def[1:])
    show_def = np.where(start_def == 1)
    numbers = in_array[show_def]
    show_def = np.array(show_def)
    show_def = np.append(show_def, len(in_array))
    length_def = np.diff(show_def)
    tup_num = np.ravel(numbers)
    tup_len = np.ravel(length_def)
    return tup_num, tup_len




