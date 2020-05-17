#/bin/python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def ldtft(h, N):
    N = int(np.fix(N))
    L = len(h)
    if (N < L):
        print('DTFT: Anzahl Datenwerte muss kleiner sein als Anzahl Stuetzstellen')
    W = (2*np.pi/N) * np.arange(0,N)
    mid = int(np.ceil(N/2))# + 1
    W[mid:N] = W[mid:N] - 2*np.pi
    W = np.fft.fftshift(W)
    H = np.fft.fftshift(np.fft.fft(h ,N))
    return H, W