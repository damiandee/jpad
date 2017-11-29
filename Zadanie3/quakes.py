import numpy as np
import csv
from statsmodels.stats.weightstats import ztest

with open('quakes.csv', 'r') as quakes:
    quakes_list = list(csv.reader(quakes, delimiter=','))
    quakes_array = np.array(quakes_list)
    depth_column = list(map(float, quakes_array[1:, 3]))
    average_depth = np.average(depth_column)
    print("Srednia glebokosc: ")
    print(average_depth)
    print("=================================================================")

    zTest = ztest(depth_column, value=300)
    print(f"P_value of the mean depth = 300 is equal to: {zTest[1]}")

    print("=================================================================")

    zTest = ztest(depth_column, value=311.371)
    print(f"P_value of the mean depth = 311.371 is equal to: {zTest[1]}")