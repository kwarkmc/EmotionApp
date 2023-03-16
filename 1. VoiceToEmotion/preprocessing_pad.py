import numpy as np

def pad1d(a, i):
    a[0:i] if a.shape[0] > i else np.hstack((a, np.zeros(i - a.shape[0])))

def pad2d(a, i):
    a[:, 0:i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0], i - a.shape[1]))))