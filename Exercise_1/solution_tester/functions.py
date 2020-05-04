import numpy as np
import matplotlib.pyplot as plt

   
def check_index_vector(variable_name, k, lenk, startv, endv):
    if len(k) != lenk:
        print('Incorrect length for ' + variable_name + '.')
        return
    elif k[0] != startv:
        print('Vector ' + variable_name + ' does not start with ' + str(startv) + '.')
        return
    elif k[-1] != endv:
        print('Vector ' + variable_name + ' does not end with ' + str(endv) + '.')
        return
    else:
        print('Index vector correct')

def check_signal_vector(variable_name, x, lenx):
    if len(x) != lenx:
        print('Incorrect length for ' + variable_name + '.')
        return
    else:
        print('Correct length for ' + variable_name + '.')
        
def check_variable(variable_name, value_cor, value_in):
    if value_cor !=value_in:
        print(variable_name + ' is not equal to ' + str(value_cor))
    else:
        print('Correct length for ' + variable_name + '.')



    
def exercise1(k, x_a, x_b, Omega_a, Omega_b):
    check_index_vector('k', k, 60, 0, 59)
    check_variable('Omega_a', 2*np.pi* 400/8000, Omega_a)
    check_signal_vector('x_a', x_a, 60)
    check_variable('Omega_b', 2*np.pi* 960/8000, Omega_b)
    check_signal_vector('x_b', x_b, 60)

def exercise2(k, x):
    check_index_vector('k', k, 16, -5, 10)
    check_signal_vector('x', x, 16)

def exercise3(k, x, kc4, xc4, kc8, xc8):
    check_index_vector('k', k, 16, 0, 15)
    check_signal_vector('x', x, 16)
    check_index_vector('kc4', kc4, 16, 4, 19)
    check_signal_vector('xc4', xc4, 16)
    check_index_vector('kc8', kc8, 16, 8, 23)
    check_signal_vector('xc8', xc8, 16)

def exercise4(k, x, x0):
    check_index_vector('k', k, 64, 0, 63)
    check_signal_vector('x', x, 64)
    check_signal_vector('x0', x0, 128)
