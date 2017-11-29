import numpy as np
import csv
from scipy import stats

with open('iris.data', 'r') as iris:
    iris_list = list(csv.reader(iris, delimiter=','))
    iris_array = np.array(iris_list)
    viriginica_list = []
    versicolor_list = []

    for flower in iris_array:
        if flower[4] == 'Iris-versicolor':
            versicolor_list.append(float(flower[1]))
        elif flower[4] == 'Iris-virginica':
            viriginica_list.append(float(flower[1]))

viriginica_array = np.array(viriginica_list)
versicolor_array = np.array(versicolor_list)

t, p = stats.ttest_ind(viriginica_array, versicolor_array)
print("t = " + str(t))
print("p = " + str(p))