import numpy as np
import csv
import pylab as pl
from scipy import stats

with open('iris.data', 'r') as iris:
    iris_list = list(csv.reader(iris, delimiter=','))
    iris_array = np.array(iris_list)
    virginica_list = []
    versicolor_list = []

    for flower in iris_array:
        if flower[4] == 'Iris-versicolor':
            versicolor_list.append(float(flower[1]))
        elif flower[4] == 'Iris-virginica':
            virginica_list.append(float(flower[1]))

virginica_array = np.array(virginica_list)
versicolor_array = np.array(versicolor_list)

virginica_array.sort()
versicolor_array.sort()

fig = pl.figure()
ax1 = fig.add_subplot(3, 1, 1)
virginica_fit = stats.norm.pdf(virginica_array, np.mean(virginica_array), np.std(virginica_array))
ax1.set_title("Virginica")
ax1.plot(virginica_array, virginica_fit, '-o')
ax1.hist(virginica_array, normed=True)


ax2 = fig.add_subplot(3, 1, 3)
versicolor_fit = stats.norm.pdf(versicolor_array, np.mean(versicolor_array), np.std(versicolor_array))
ax2.set_title("Versicolor")
ax2.plot(versicolor_array, versicolor_fit, '-o')
ax2.hist(versicolor_array, normed=True)
pl.show()

print("Średnia wartość dla Iris Virginica = " + str(np.mean(virginica_array)))
print("Średnia wartość dla Iris Versicolor = " + str(np.mean(versicolor_array)))

t, p = stats.ttest_ind(virginica_array, versicolor_array)
print("t = " + str(t))
print("p = " + str(p))

if p < 0.05:
    print("\nKwiatów Iris Virginica oraz Iris Versicolor nie da się rozróżnić na podstawie atrybutu 'sepal width'")
else:
    print("\nKwiaty Iris Virginica oraz Iris Versicolor można rozróżnić na podstawie atrybutu 'sepal width'")
