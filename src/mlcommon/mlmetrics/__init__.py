import numpy as np
import matplotlib.pyplot as plt


def true_positives(c, y_pred, y_true):
    t_indexes = np.where(y_true == c)
    tp = np.count_nonzero(y_pred[t_indexes] == c)
    return tp


def true_negatives(c, y_pred, y_true):
    n_indexes = np.where(y_true != c)
    tn = np.count_nonzero(y_pred[n_indexes] != c)
    return tn


def false_positives(c, y_pred, y_true):
    p_indexes = np.where(y_pred == c)
    fp = np.count_nonzero(y_true[p_indexes] != c)
    return fp


def false_negatives(c, y_pred, y_true):
    n_indexes = np.where(y_pred != c)
    fn = np.count_nonzero(y_true[n_indexes] == c)
    return fn


def calculate_confusion_matrix(y_true, y_pred):
    classes = np.unique(y_true)
    cm = np.zeros((len(classes), len(classes)), dtype=int)
    for tl in classes:
        true_ind = np.where(y_true == tl)
        pred = y_pred[true_ind]
        for pl in classes:
            cm[tl, pl] = np.count_nonzero(pred == pl)

    return cm


# Taken from https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
def plot_confusion_matrix(y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = calculate_confusion_matrix(y_true, y_pred)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()

    return ax
