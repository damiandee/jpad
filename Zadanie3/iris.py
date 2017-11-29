import numpy as np
import csv
import pylab as pl
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

viriginica_array.sort()
versicolor_array.sort()

fig = pl.figure()
ax1 = fig.add_subplot(3, 1, 1)
viriginica_fit = stats.norm.pdf(viriginica_array, np.mean(viriginica_array), np.std(viriginica_array))
ax1.set_title("Virginica")
ax1.plot(viriginica_array, viriginica_fit, '-o')
ax1.hist(viriginica_array, normed=True)


ax2 = fig.add_subplot(3, 1, 3)
versicolor_fit = stats.norm.pdf(versicolor_array, np.mean(versicolor_array), np.std(versicolor_array))
ax2.set_title("Versicolor")
ax2.plot(versicolor_array, versicolor_fit, '-o')
ax2.hist(versicolor_array, normed=True)
pl.show()

t, p = stats.ttest_ind(viriginica_array, versicolor_array)
print("t = " + str(t))
print("p = " + str(p))

if p < 0.05:
    print("\nKwiaty Iris Viriginica oraz Iris Versicolor można rozróżnić na podstawie atrybutu 'sepal width'")
else:
    ("Kwiatów nie da się rozróżnić na podstawie atrybutu 'sepal width'")
