import numpy as np
import scipy.sparse as sp

def HilbertМatrix(k):
    matrix = [[(1 / (i + j + 1)) for i in range(k)] for j in range(k)]
    return matrix
