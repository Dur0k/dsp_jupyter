import numpy as np
import matplotlib.pyplot as plt
from . import testfunctions as test


def exercise1(k, x_a, x_b, Omega_a, Omega_b):
    test.check_index_vector('k', k, 60, 0, 59)
    test.check_variable('Omega_a', 2*np.pi* 400/8000, Omega_a)
    test.check_signal_vector('x_a', x_a, 60)
    test.check_variable('Omega_b', 2*np.pi* 960/8000, Omega_b)
    test.check_signal_vector('x_b', x_b, 60)

def exercise2(k, x):
    test.check_index_vector('k', k, 16, -5, 10)
    test.check_signal_vector('x', x, 16)

