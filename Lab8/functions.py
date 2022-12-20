import random
import numpy as np
import pandas as pd


def generate_data(size):
    return pd.DataFrame(data={'x': [random.uniform(-1, 1) for i in range(size)],
                              'y': [random.uniform(-1, 1) for i in range(size)]})


def accuracy(true, pred):
    return np.sum(true == pred) / len(true)


def precision(true, pred):
    tp = np.sum((true == 1) & (pred == 1))
    fp = np.sum((true == 0) & (pred == 1))
    return tp / (tp + fp)


def recall(true, pred):
    tp = np.sum((true == 1) & (pred == 1))
    fn = np.sum((true == 1) & (pred == 0))
    return tp / (tp + fn)


def f_measure(true, pred):
    p = precision(true, pred)
    r = recall(true, pred)
    return 2 * (p * r) / (p + r)
