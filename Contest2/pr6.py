"""PR 6"""
import numpy as np


def get_best_indices(ranks: np.ndarray, top: int, axis: int = 1) -> np.ndarray:
    """DEF"""
    arr_len = ranks.shape[axis]
    tmp_arr = np.argpartition(ranks, arr_len - top, axis=axis)
    tmp_val = np.partition(ranks, arr_len - top, axis=axis)
    tmp_val = np.take(tmp_val, arr_len - top + np.arange(top), axis=axis)
    tmp_arr = np.take(tmp_arr, arr_len - top + np.arange(top), axis=axis)
    tmp_arr = np.take_along_axis(tmp_arr, np.argsort(-tmp_val, axis=axis), axis=axis)
    return tmp_arr


if __name__ == "__main__":
    with open('input.bin', 'rb') as f_data:
        ranks = np.load(f_data)
        indices = get_best_indices(ranks, 5)
    with open('output.bin', 'wb') as f_data:
        np.save(f_data, indices)

