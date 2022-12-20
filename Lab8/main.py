import matplotlib.pyplot as plt
import sklearn.model_selection
from sklearn import svm

import functions


def testing_data_size():
    test_range = range(1000, 100001, 10000)
    accuracies, precisions, recalls, f1scores = [], [], [], []
    for i in test_range:
        data = functions.generate_data(i)
        data = data.assign(ans=data.x ** 2 + data.y ** 2 < 0.25)
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


if __name__ == '__main__':
    testing_data_size()
