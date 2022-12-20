import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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


def f_score(true, pred):
    p = precision(true, pred)
    r = recall(true, pred)
    return 2 * (p * r) / (p + r)


def print_all_metrics(true, pred):
    metrics = pd.Series(data={'accuracy': accuracy(true, pred),
                              'precision': precision(true, pred),
                              'recall': recall(true, pred),
                              'F1 score': f_score(true, pred)})
    print(metrics)


def plot_data(data):
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#32a1ce', '#121212'])
    sns.scatterplot(x='x', y='y', hue='ans', data=data)
    plt.show()