import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def getMaxCorrCoef(feats):
    feats[0] = np.array(feats[0]).astype(np.float)
    feats[1] = np.array(feats[1]).astype(np.float)
    feats[2] = np.array(feats[2]).astype(np.float)
    feats[3] = np.array(feats[3]).astype(np.float)
    feats[4] = np.array(feats[4]).astype(np.float)
    feats[5] = np.array(feats[5]).astype(np.float)
    feats[6] = np.array(feats[6]).astype(np.float)
    feats[7] = np.array(feats[7]).astype(np.float)

    featsNumber = len(feats)

    maxCoef = 0.0
    f1 = 0
    f2 = 0

    for i in range(featsNumber):
        for j in range(i + 1, (featsNumber)):
            coef = np.corrcoef(feats[i], feats[j])[0, 1]

            if(coef > maxCoef):
                maxCoef = coef
                f1 = i
                f2 = j

    return ([f1, f2])



def makeHistogram(abalone_array):
    data = abalone_array

    featNames = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings']
    length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight, rings = data.T[1:]
    feats = [length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight, rings]
    featIndex = getMaxCorrCoef(feats)

    plt.xlabel(featNames[featIndex[0]])
    plt.title('Histogram cechy: ' + featNames[featIndex[0]])
    plt.hist(feats[featIndex[0]], 150, normed=1, facecolor='g', alpha=0.75)

    plt.title('Histogram cechy: ' + featNames[featIndex[1]])
    plt.xlabel(featNames[featIndex[1]])
    plt.hist(feats[featIndex[1]], 150, normed=1, facecolor='r', alpha=0.75)

    plt.xlim([0, 1])
    plt.plot(linregress(feats[featIndex[0]], feats[featIndex[1]]), color='blue')
    plt.show()
