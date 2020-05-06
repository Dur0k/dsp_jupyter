import matplotlib.pyplot as plt
from  matplotlib import patches
import numpy as np

def zplane(b,a):
    '''
    Plot the poles and zeros on a complex plane. b and a are the polynomial coefficients of the following transfer function:
    H(z) = B(z)/A(z) = (b0 + b1 z^(-1) + b2 z^(-2) + ... + bM z^(-M)) / (a0 + a1 z^(-1) + a2 z^(-2) + ... + aN z^(-N))
    '''
    fig, axs = plt.subplots(1, 1, figsize=(6, 6))
    uc = patches.Circle((0,0), radius=1, fill=False, color='black')
    axs.add_patch(uc)
    axs.set_xlim((-1.1,1.1))
    axs.set_ylim((-1.1,1.1))
    axs.grid(True, color='0.9', linestyle='-', which='major', axis='both')
    axs.axis('scaled')
    axs.axis([-1.2, 1.2, -1.2, 1.2])
    axs.set_title(r'Pole-Zero Plot')
    b = np.asarray(b)
    a = np.asarray(a)
    z = np.roots(b)     # calculate zeros while interpreting b as polynomial coefficients
    p = np.roots(a)     # calculate poles with a
    z_plt = plt.plot(z.real, z.imag, 'o', markersize=8, mfc='none', color = '#5698c6', mew=2)
    p_plt = plt.plot(p.real, p.imag, 'x', markersize=8, color = '#5698c6', mew=2)
    plt.plot()
    

def zplane_ax(b,a,axs):
    '''
    Plot the poles and zeros on a complex plane. b and a are the polynomial coefficients of the following transfer function:
    H(z) = B(z)/A(z) = (b0 + b1 z^(-1) + b2 z^(-2) + ... + bM z^(-M)) / (a0 + a1 z^(-1) + a2 z^(-2) + ... + aN z^(-N))
    '''
    #fig, axs = plt.subplots(1, 1, figsize=(6, 6))
    uc = patches.Circle((0,0), radius=1, fill=False, color='black')
    axs.add_patch(uc)
    axs.set_xlim((-1.1,1.1))
    axs.set_ylim((-1.1,1.1))
    axs.grid(True, color='0.9', linestyle='-', which='major', axis='both')
    axs.axis('scaled')
    axs.axis([-1.2, 1.2, -1.2, 1.2])
    axs.set_title(r'Pole-Zero Plot')
    b = np.asarray(b)
    a = np.asarray(a)
    z = np.roots(b)     # calculate zeros while interpreting b as polynomial coefficients
    p = np.roots(a)     # calculate poles with a
    axs.plot(z.real, z.imag, 'o', markersize=8, mfc='none', color = '#5698c6', mew=2)
    axs.plot(p.real, p.imag, 'x', markersize=8, color = '#5698c6', mew=2)

