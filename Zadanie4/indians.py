from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import pylab as pl
import warnings

warnings.filterwarnings('ignore', 'Solver terminated early.*')
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
dataset = np.loadtxt('pima-indians-diabetes.data', delimiter=",")

X = dataset[:, 0:7]
y = dataset[:, 8]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

fig = pl.figure()

def compute_svm(iterations):
    print("\nSVM")
    svm = SVC(max_iter=iterations)
    svm.fit(X_train, y_train)
    print(svm)

    expected = y_test
    predicted = svm.predict(X_test)

    svm_confussion_matrix = metrics.confusion_matrix(expected, predicted)

    return accuracy_score(y_test, predicted) * 100


def compute_knn(iterations):
    print("\nKNN")
    knn = KNeighborsClassifier(iterations)
    knn.fit(X_train, y_train)
    print(knn)

    expected = y_test
    predicted = knn.predict(X_test)

    # print(metrics.classification_report(expected, predicted))
    knn_confussion_matrix = metrics.confusion_matrix(expected, predicted)
    print(accuracy_score(y_test, predicted) * 100)

    return accuracy_score(y_test, predicted) * 100
##############################################################


svm_correct = []

# SVM
for i in range(1, 51):
    iterations = i * 10
    svm_correct.append([iterations, compute_svm(iterations)])

svm_correct = np.array(svm_correct)
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_title("SVM")
ax1.plot(svm_correct[:, 0], svm_correct[:, 1])
##############################################################

# KNN

knn_correct = []

for i in range(1, 51):
    iterations = i * 10
    knn_correct.append([iterations, compute_knn(iterations)])

knn_correct = np.array(knn_correct)
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(knn_correct[:, 0], knn_correct[:, 1])

pl.show()
