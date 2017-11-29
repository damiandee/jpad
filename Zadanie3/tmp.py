## Import the packages
import numpy as np
import csv
from scipy import stats
from scipy.stats import ttest_ind, ttest_ind_from_stats

with open('iris.data', 'r') as iris:
    iris_list = list(csv.reader(iris, delimiter=','))
    iris_array = np.array(iris_list)
    viriginica_list = []
    versicolor_list = []

    for flower in iris_array :
        if flower[4] == 'Iris-versicolor':
            versicolor_list.append(float(flower[1]))
        elif flower[4] == 'Iris-virginica':
            viriginica_list.append(float(flower[1]))

    print(versicolor_list)
    print(viriginica_list)

N = viriginica_list.__sizeof__()
viriginica_array = np.array(viriginica_list)
versicolor_array = np.array(versicolor_list)
## Calculate the Standard Deviation
#Calculate the variance to get the standard deviation

#For unbiased max likelihood estimate we have to divide the var by N-1, and therefore the parameter ddof = 1
var_versicolor = versicolor_array.var(ddof=1)
var_virginica = viriginica_array.var(ddof=1)

#std deviation
s = np.sqrt((var_versicolor + var_virginica) / 2)
s



## Calculate the t-statistics
t = (versicolor_array.mean() - viriginica_array.mean())/(s*np.sqrt(2/N))



## Compare with the critical t-value
#Degrees of freedom
df = 2*N - 2

#p-value after comparison with the t
p = 1 - stats.t.cdf(t,df=df)


print("t = " + str(t))
print("p = " + str(2*p))
#Note that we multiply the p value by 2 because its a twp tail t-test
### You can see that after comparing the t statistic with the critical t value (computed internally) we get a good p value of 0.0005 and thus we reject the null hypothesis and thus it proves that the mean of the two distributions are different and statistically significant.


## Cross Checking with the internal scipy function
t2, p2 = stats.ttest_ind(versicolor_array, viriginica_array)
print("t = " + str(t2))
print("p = " + str(2*p2))

te, pe = ttest_ind(viriginica_array, versicolor_array, equal_var=False)
print("te = " + str(te))
print("pe = " + str(pe))