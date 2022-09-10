import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import average_precision_score, roc_auc_score, precision_recall_curve, roc_curve, precision_score, recall_score, f1_score


def ks_stat(y_true, y_score):
    return ks_2samp(y_score[y_true==1], y_score[y_true!=1]).statistic


def score(y_test, y_score, show_plot=True, score_lim=20):
    precision, recall, thresholds = precision_recall_curve(y_true=y_test, probas_pred=y_score)
    f_score = (2 * precision * recall) / (precision + recall)
    f_score[np.isnan(f_score)] = 0
    ix = np.argmax(f_score)
    best_threshold = thresholds[ix]
    best_f1 = f_score[ix]
    best_precision = precision[ix]
    best_recall = recall[ix]
    
    # given_f1 = f1_score(y_test, y_score>model_conf["threshold_score"])
    # given_precision = precision_score(y_test, y_score>model_conf["threshold_score"])
    # given_recall = recall_score(y_test, y_score>model_conf["threshold_score"])

    fpr, tpr, thresholds = roc_curve(y_true=y_test, y_score=y_score)

    # print("best_threshold ", best_threshold)
    # print("best F1 ", best_f1)
    # print("precision ", best_precision)
    # print("recall ", best_recall)
     
    print("average precision ", average_precision_score(y_true=y_test, y_score=y_score))
    print("roc_auc_score ", roc_auc_score(y_true=y_test, y_score=y_score))
    print("ks_stat ", ks_stat(y_true=y_test, y_score=y_score))
    if not show_plot:
      return
    sns.kdeplot(y_score[y_test==1], label="1")
    sns.kdeplot(y_score[y_test==0], label="0")
    plt.legend()
    plt.show()
    sns.displot(
        pd.DataFrame({"score": y_score,"class": y_test}),
        x="score",
        hue="class",
        hue_order=[1, 0]
      )
    plt.ylim([0, score_lim])
    plt.show()
    plt.plot(recall, precision)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.plot([recall[ix]],[precision[ix]], "r*")
    plt.show()
    plt.plot(fpr, tpr, color="orange")
    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()  