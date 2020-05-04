import numpy as np
import matplotlib.pyplot as plt


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

def check_vector(variable_name, value_cor, value_in):
    if not np.allclose(value_cor, value_in):
        print(variable_name + ' is not correct.')



    
def exercise1b(y_resp):
    check_vector('y_resp', np.array(([1.,2.5,3.,1.75,0.25,-0.625,-0.75,-0.4375,-0.0625,0.15625])), y_resp)
   

def exercise1c(filtersystem):
    y_resp = np.array(([1.,2.5,3.,1.75,0.25,-0.625,-0.75,-0.4375,-0.0625,0.15625]))
    x = np.zeros(10)
    x[0] = 1
    y = filtersystem(x)
    if len(y) != len(y_resp):
        print('Function needs to return as many output samples as input samples.')
    if not np.allclose(y_resp, y):
        print('Function filtersystem() does not return the correct impulse response.')

def exercise1d(a, b):
    check_vector('a', np.array(([1., -1., 0.5])) , a)
    check_vector('b', np.array(([1., 1.5, 1.])) , b)

def exercise2a(k, x, a, b, y):
    check_index_vector('k', k, 111, -10, 100)
    check_signal_vector('x', x, 111)
    check_signal_vector('y', y, 111)
    check_vector('a', np.array(([1, -1.8*np.cos(np.pi/16), 0.81])) , a)
    check_vector('b', np.array(([1, 0.5])) , b)
    
def exercise3(Wp, Ws):
    fD = 1000
    fS = 1400
    fA = 8000
    Wp_c = 2*fD/fA
    Ws_c = 2*fS/fA
    check_variable('Wp', Wp_c, Wp)
    check_variable('Ws', Ws_c, Ws)
