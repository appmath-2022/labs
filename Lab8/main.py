import matplotlib.pyplot as plt
import numpy as np
import sklearn.model_selection
from sklearn import svm
import functions


def testing_data_size():
    test_range = range(1000, 100001, 10000)
    accuracies, precisions, recalls, f1scores = [], [], [], []
    for i in test_range:
        data = functions.generate_data(i)
        X = data[['x', 'y']]
        y = data['ans']
        X_train, X_test, y_train, y_test = \
            sklearn.model_selection.train_test_split(X, y)
        clf = svm.NuSVC(gamma="auto", nu=0.09, kernel='rbf')
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print("Размер выборки = ", i)
        accuracies.append(functions.accuracy(y_test, y_pred))
        precisions.append(functions.precision(y_test, y_pred))
        recalls.append(functions.recall(y_test, y_pred))
        f1scores.append(functions.f_score(y_test, y_pred))
        functions.print_all_metrics(y_test, y_pred)
    plt.plot(test_range, accuracies)
    plt.legend(["accuracy"])
    plt.show()
    plt.plot(test_range, precisions)
    plt.legend(["precision"])
    plt.show()
    plt.plot(test_range, recalls)
    plt.legend(["recall"])
    plt.show()
    plt.plot(test_range, f1scores)
    plt.legend(["f1 score"])
    plt.show()


def testing_kernels():
    data = functions.generate_data(20000)
    X = data[['x', 'y']]
    y = data['ans']
    X_train, X_test, y_train, y_test = \
        sklearn.model_selection.train_test_split(X, y)
    for kernel in ['linear', 'poly', 'rbf', 'sigmoid']:
        clf = svm.NuSVC(gamma="auto", nu=0.09, kernel=kernel, degree=2)
        clf.fit(X_train.values, y_train.values)
        y_pred = clf.predict(X_test.values)
        print(kernel)
        functions.print_all_metrics(y_test, y_pred)
        functions.plot_decision_function(clf.decision_function, X_test, y_pred, title=kernel)


def testing_lower_bound():
    data = functions.generate_data(20000)
    X = data[['x', 'y']]
    y = data['ans']
    X_train, X_test, y_train, y_test = \
        sklearn.model_selection.train_test_split(X, y)
    test_range = np.arange(0.01, 1.01, 0.01)
    accuracies, precisions, recalls, f1scores = [], [], [], []
    for nu in test_range:
        try:
            clf = svm.NuSVC(gamma="auto", nu=nu, kernel='rbf')
            clf.fit(X_train.values, y_train.values)
            y_pred = clf.predict(X_test.values)
            accuracies.append(functions.accuracy(y_test, y_pred))
            precisions.append(functions.precision(y_test, y_pred))
            recalls.append(functions.recall(y_test, y_pred))
            f1scores.append(functions.f_score(y_test, y_pred))
        except ValueError:
            accuracies.append(accuracies[-1])
            precisions.append(precisions[-1])
            recalls.append(recalls[-1])
            f1scores.append(f1scores[-1])
            pass

    plt.plot(test_range, accuracies)
    plt.legend(["accuracy"])
    plt.show()
    plt.plot(test_range, precisions)
    plt.legend(["precision"])
    plt.show()
    plt.plot(test_range, recalls)
    plt.legend(["recall"])
    plt.show()
    plt.plot(test_range, f1scores)
    plt.legend(["f1 score"])
    plt.show()


if __name__ == '__main__':
    testing_data_size()
    testing_kernels()
    testing_lower_bound()