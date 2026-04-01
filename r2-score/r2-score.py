import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype = float)
    y_pred = np.asarray(y_pred, dtype = float)
    
    mean = np.mean(y_true)
    SSres = np.sum((y_true - y_pred) ** 2)
    SStot = np.sum((y_true - mean) ** 2)

    if SStot == 0:
        if np.sum(y_pred == y_true) == len(y_true):
            return 1.0
        else:
            return 0.0
            
    R2 = 1 - (SSres / SStot)   
    return R2
    pass