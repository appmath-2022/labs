import sklearn.model_selection
from sklearn import svm

import functions


if __name__ == '__main__':
    data = functions.generate_data(10000)
    data = data.assign(ans=data.x ** 2 + data.y ** 2 < 0.25)
    X = data[['x', 'y']]
    y = data['ans']
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.4)
    clf = svm.NuSVC(gamma="auto", nu=0.09, kernel='rbf')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    functions.print_all_metrics(y_test, y_pred)
    functions.plot_data(data)