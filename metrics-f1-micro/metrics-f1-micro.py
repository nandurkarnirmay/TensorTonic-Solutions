import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype = int)
    y_pred = np.asarray(y_pred, dtype = int)
    n = y_true.size
    TP = np.sum(y_pred == y_true)
    FP = n - TP
    FN = FP

    F1 = (2* TP) / (2 * TP + FP + FN)
    return F1
    pass