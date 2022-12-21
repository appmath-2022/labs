import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def generate_data(size):
    data = pd.DataFrame(data={'x': [random.uniform(-1, 1) for i in range(size)],
                              'y': [random.uniform(-1, 1) for i in range(size)]})
    return data.assign(ans=data.x ** 2 + data.y ** 2 < 0.25)


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


def plot_decision_function(decision_function, X, Y, title=None):
    xx, yy = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
    decision_result = decision_function(np.c_[xx.ravel(), yy.ravel()])
    decision_result = decision_result.reshape(xx.shape)
    plt.imshow(
        decision_result,
        interpolation='nearest',
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        aspect='auto',
        origin='lower'
    )

    plt.contour(
        xx,
        yy,
        decision_result,
        levels=[0],
    )

    plt.scatter(
        X['x'],
        X['y'],
        c=Y,
        edgecolors='k'
    )

    plt.title(title)
    plt.axis([-1, 1, -1, 1])
    plt.show()