import numpy as np
import matplotlib.pyplot as plt
from . import testfunctions as test

    
def exercise1(Omega0, k, xsin, Omega0b, kb, xsinb):
   test.check_variable('Omega0', 2*np.pi* 400/8000, Omega0)
   test.check_index_vector('k', k, 60, 0, 59)
   test.check_signal_vector('xsin', xsin, 60)
   test.check_variable('Omega0b', 2*np.pi* 960/8000, Omega0b)
   test.check_index_vector('kb', kb, 0, 59)
   test.check_signal_vector('xsinb', xsinb, 60)

def exercise2(kk08, kk64, x1_08, x1_64, x2_08, x2_64, x3_08, x3_64):
   test.check_index_vector('kk08', kk08, 8, 0, 7)
   test.check_index_vector('kk64', kk64, 64, 0, 63)
   test.check_signal_vector('x1_08', x1_08, 8)
   test.check_signal_vector('x1_64', x1_64, 64)
   test.check_signal_vector('x2_08', x2_08, 8)
   test.check_signal_vector('x2_64', x2_64, 64)
   test.check_signal_vector('x3_08', x3_08, 8)
   test.check_signal_vector('x3_64', x3_64, 64)

def exercise3(kk, x1, x2):
    test.check_index_vector('kk', kk, 16, 0, 63)
    test.check_signal_vector('x1', x1, 64)
    test.check_signal_vector('x2', x2, 64)

def exercise4(k, x, x0):
    test.check_index_vector('k', k, 64, 0, 63)
    test.check_signal_vector('x', x, 64)
    test.check_signal_vector('x0', x0, 128)
