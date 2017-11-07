import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def get_max_corr_coef(feats):
    feats[0] = np.array(feats[0]).astype(np.float)
    feats[1] = np.array(feats[1]).astype(np.float)
    feats[2] = np.array(feats[2]).astype(np.float)
    feats[3] = np.array(feats[3]).astype(np.float)
    feats[4] = np.array(feats[4]).astype(np.float)
    feats[5] = np.array(feats[5]).astype(np.float)
    feats[6] = np.array(feats[6]).astype(np.float)
    feats[7] = np.array(feats[7]).astype(np.float)

    feats_number = len(feats)

    max_coef = 0.0
    f1 = 0
    f2 = 0

    for i in range(feats_number):
        for j in range((i + 1), feats_number):
            coef = np.corrcoef(feats[i], feats[j])[0, 1]

            if(coef > max_coef):
                max_coef = coef
                f1 = i
                f2 = j

    return [f1, f2]


def make_histogram(abalone_array):
    data = abalone_array

    feat_names = ['length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings']
    length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight, rings = data.T[1:]
    feats = [length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight, rings]
    feat_index = get_max_corr_coef(feats)

    plt.xlabel(feat_names[feat_index[0]])
    plt.title('Histogram')
    plt.hist(feats[feat_index[0]], 150, facecolor='g')

    plt.xlabel(feat_names[feat_index[1]])
    plt.hist(feats[feat_index[1]], 150, facecolor='r')

    plt.legend(((feat_names[feat_index[0]]), (feat_names[feat_index[1]])), loc=(1.005, 0.5))
    plt.xlim([0, 1])
    plt.ylim([0, 140])
    plt.plot(linregress(feats[feat_index[0]], feats[feat_index[1]]), color='blue')
    plt.show()