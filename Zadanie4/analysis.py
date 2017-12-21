import matplotlib.pyplot as plt
import pandas
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from helpers import plot_learning_curve
from sklearn.svm import SVC


def classifiers_comparison():
    names = ["KNN", "SVM"]

    classifiers = [
        KNeighborsClassifier(),
        SVC()
    ]

    dataset = pandas.read_csv('pima-indians-diabetes.data')

    print("DataSet Shape:")
    print(dataset.shape)
    print("DataSet Stats:")
    print(dataset.describe(include='all'))

    i = 1

    X, y = dataset.iloc[:, 0:-1], dataset.iloc[:, -1]

    pca = PCA(n_components=2)
    X = pca.fit_transform(X)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=.4, random_state=42)

    fig = plt.figure()

    for name, clf in zip(names, classifiers):
        clf.fit(X_train, y_train)
        if i < 6:
            fig.add_subplot(2, len(classifiers) / 2 + 1, i)
        else:
            fig.add_subplot(2, len(classifiers) / 2 + 1, i)

        plot_learning_curve(clf, name, X_test, y_test)
        i += 1
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.3, hspace=0.2)
    plt.show()


classifiers_comparison()
