#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 15:09:38 2018

@author: bernardo
"""

import matplotlib.pyplot as plt
import numpy as np
#%matplotlib auto
#%pylab

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 10,
        }

dt=np.genfromtxt('data_files/90us_sinal2.txt',dtype=np.int16)
Fs=1.0/90e-6
#dt=np.genfromtxt('data_files/173hz_sinal2.txt',dtype=np.int16)
#  2*173 - 420 = -74
#  3*173 - 460 = 59
#  3*173 - 440  = 79
#Fs=173.0
#dt=np.genfromtxt('data_files/173hz_sinalcomplexo.txt',dtype=np.int16)
#Fs=173.0

Ts=1/Fs

dt = dt - 512

signal=dt[:,1]
n = len(signal) # length of the signal
#plt.plot(x, signal )
# matplotlib.org/examples/pylab_examples/subplots_demo.html
# Two subplots, the axes array is 1-d
plt.close('all')
f, (ax1, ax2) = plt.subplots(2, sharex=False)


Y = np.fft.fft(signal)/n # fft computing and normalization
Y = Y[range(int(n/2))] # n//2 perform integer division
#fig, ax = plt.subplots(2, 1)
k= np.arange(n)
T= n/Fs
frq= k/T # two sides frequency range
frq=frq[range(int(n/2))] # one side frequency range
#plt.clf()

ax1.plot(signal,'b') # plotting the spectrum

ax2.plot(frq,abs(Y),'r') # plotting the spectrum
ax2.set_xlabel('Freq / Hz')
#plt.text(40, 20, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
#ax2.text(40, 20, r'3*173-460=59', fontdict=font)
#ax2.text(52, 25, r'2*173-420=-74', fontdict=font)
#ax2.text(55, 60, r'3*173-440=79', fontdict=font)

#plt.title('complex signal ')
#plt.title(r'AM Signal, 440 $\pm$ 20 Hz')
#plt.grid()

plt.show()
