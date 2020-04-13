import numpy as np
import matplotlib.pyplot as plt


def print_sine(f):
    '''
    Function to display a sine of frequency f. Uses matplotlib and numpy.
    '''
    x = np.arange(100)
    y = np.sin(2*np.pi*x*f)
    plt.plot(x,y)
    plt.show()


def print_exp(f):
    '''
    Function to display exponential function with frequency f. Uses matplotlib and numpy.
    '''
    x = np.arange(100)
    y = np.exp(2*np.pi*x*f)
    plt.plot(x,y)
    plt.show()
   
def check_index_vector(variable_name, k, lenk, startv, endv):
    if len(k) != lenk:
        print('Incorrect length for ' + variable_name + '.')
        return
    if k[0] != startv:
        print('Vector ' + variable_name + ' does not start with ' + str(startv) + '.')
        return
    if k[-1] != endv:
        print('Vector ' + variable_name + ' does not end with ' + str(endv) + '.')
        return

def check_signal_vector(variable_name, x, lenx):
    if len(x) != lenx:
        print('Incorrect length for ' + variable_name + '.')
        return
        
def check_variable(variable_name, value_cor, value_in):
    if value_cor !=value_in:
        print(variable_name + ' is not equal to ' + str(value_cor))




    
def exercise1(Omega0, k, xsin, Omega0b, kb, xsinb):
   check_variable('Omega0', 2*np.pi* 400/8000, Omega0)
   check_index_vector('k', k, 60, 0, 59)
   check_signal_vector('xsin', xsin, 60)
   check_variable('Omega0b', 2*np.pi* 960/8000, Omega0b)
   check_index_vector('kb', kb, 0, 59)
   check_signal_vector('xsinb', xsinb, 60)

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
