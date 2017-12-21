import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve


def plot_learning_curve(estimator, title, X_test, y_test):
    plt.title(title)
    plt.xlabel("Średnia przewidywana wartość")
    plt.ylabel("Frakcja pozytywów")

    if hasattr(estimator, "predict_proba"):
        prob_pos = estimator.predict_proba(X_test)[:, 1]
    else:  # use decision function
        prob_pos = estimator.decision_function(X_test)
        prob_pos = \
            (prob_pos - prob_pos.min()) / (prob_pos.max() - prob_pos.min())
    fraction_of_positives, mean_predicted_value = \
        calibration_curve(y_test, prob_pos, n_bins=10)

    plt.plot([0, 1], [0, 1], "k:", label="Idealnie skalibrowane")

    plt.plot(mean_predicted_value, fraction_of_positives, "s-",
             label="%s" % (title, ))

    plt.legend(loc="best")
