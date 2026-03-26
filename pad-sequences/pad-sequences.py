import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    L = max_len if max_len is not None else (max(len(seq) for seq in seqs) if N > 0 else 0)

    result = np.full((N, L), fill_value = pad_value, dtype = 'float')
    for i,seq in enumerate(seqs):
        result[i, :len(seq)] = seq[: L]

    return result
    