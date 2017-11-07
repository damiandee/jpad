# Zadanie polega na przeprowadzeniu analizy statystycznej dla wskazanego zbioru danych.
#
# Wymagania na ocenę dostateczną:
# Dla podanych atrybutów wyznaczyć medianę, minimum i maximum dla cech ilościowych i dominantę dla cech jakościowych.
# Zadbać o czytelność rezultatów.
#
# Wymagania na ocenę dobrą:
# Narysować histogramy dla dwóch cech ilościowych najbardziej ze sobą skorelowanych.
# Zadbać o czytelność rezultatów oraz staranny i atrakcyjny wygląd histogramów.
#
# Wymagania na ocenę bardzo dobrą:
# Wyznaczyć i narysować krzywą regresji dla dwóch cech ilościowych najbardziej ze sobą skorelowanych.
# Zadbać o czytelność rezultatów oraz staranny i atrakcyjny wygląd wykresów.

#w konsoli pip install numpy

from PlotManager import getMaxCorrCoef

import numpy as np
import csv
from PlotManager import makeHistogram

with open('abalone.data', 'r') as abalone_file:
    abalone_list = list(csv.reader(abalone_file, delimiter=','))
    abalone_array = np.array(abalone_list)
    numericColumn1 = abalone_array[:, 1]
    numericColumn2 = abalone_array[:, 2]
    numericColumn3 = abalone_array[:, 3]
    numericColumn4 = abalone_array[:, 4]
    numericColumn5 = abalone_array[:, 5]
    numericColumn6 = abalone_array[:, 6]
    numericColumn7 = abalone_array[:, 7]
    numericColumn8 = abalone_array[:, 8]
print("==============================")
print("MEDIANA")
print("==============================")

for i in range(1, 9):
    numericColumn = abalone_array[:, i]
    median = np.median(list(map(float, numericColumn)))
    print("Mediana " + str(i) + " kolumny wynosi: " + str(median))

print("==============================")
print("MINIMUM")
print("==============================")

for i in range(1, 9):
    numericColumn = abalone_array[:, i]
    min = np.min(list(map(float, numericColumn)))
    print("Minimum " + str(i) + " kolumny wynosi: " + str(min))

print("==============================")
print("MAKSIMUM")
print("==============================")

for i in range(1, 9):
    numericColumn = abalone_array[:, i]
    max = np.max(list(map(float, numericColumn)))
    print("Maksimum " + str(i) + " kolumny wynosi: " + str(max))



textColumn = list(abalone_array[:, 0])

countM = textColumn.count("M")
countF = textColumn.count("F")
countI = textColumn.count("I")

minimum = countM
if countF > countM and countF > countI:
    print("Dominanta wynosi (F): " + str(countF))
elif countM > countF and countM > countI:
    print("Dominanta wynosi (M): " + str(countM))
elif countI > countF and countI > countM:
    print("Dominanta wynosi (I): " + str(countI))



print("Ilość wystąpień M: " + str(countM))
print("Ilość wystąpień F: " + str(countF))
print("Ilość wystąpień I: " + str(countI))

print('===========================================================================')

makeHistogram(abalone_array)






