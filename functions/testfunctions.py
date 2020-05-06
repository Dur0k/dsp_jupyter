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
        
def check_vector(variable_name, value_cor, value_in):
    if not np.allclose(value_cor, value_in):
        print(variable_name + ' is not correct.')
