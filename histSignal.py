#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 17:44:52 2018

@author: bernardo

Ajuste de função ao histograma
Adaptado de:
https://www.maximintegrated.com/en/app-notes/index.mvp/id/2085

"""

import matplotlib.pyplot as plt
import numpy as np
#%matplotlib auto
#%pylab

#dt=np.genfromtxt('data_files/90us_sinal2.txt',dtype=np.int16)
#Fs=1.0/90e-6
#dt=np.genfromtxt('data_files/173hz_sinal2.txt',dtype=np.int16)
#  2*173 - 420 = -74
#  3*173 - 460 = 59
#  3*173 - 440  = 79
#Fs=173.0
Nbit=10
Nsteps=2**Nbit-1
dt=np.genfromtxt('data_files/10kamostra_100hz.txt',dtype=np.int16)

#Fs=173.0
#Ts=1/Fs

#dt = dt - 512

signal=dt[:,1]
n = len(signal) # length of the signal

plt.clf()

Nbit=10

# matplotlib.org/examples/pylab_examples/subplots_demo.html
# Two subplots, the axes array is 1-d
plt.close('all')
f, (ax1, ax2) = plt.subplots(2, sharex=True)

# the histogram of the data
val, bins, patches = ax1.hist(signal, bins=Nsteps, range =(0,1023),   facecolor='g', alpha=0.75)


ax1.set_xlabel('ADC code')
ax1.set_ylabel('Counts')
ax1.set_title('Histogram of Sinus Signal 50k points')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
ax1.grid(True)


# codigo minimo do histograma
hmin=argmax(val[0:Nsteps//2])
#hmin=np.min(signal)
# codigo maximo do histograma
#hmax=np.max(signal)
hmax=argmax(val[Nsteps//2: -1]) + Nsteps//2
#gama de valores na abcissas (garantir que o argumento de asin <= 1)
xd = np.arange((hmin+1),hmax) # remove first point singularity
#valor central do sinal seno
C=(hmax+hmin)/2.0
#Amplitude do seno
A=hmax-hmin
#funcao de ajuste
hteor=(np.arcsin(2.0*(xd-C)/A) - np.arcsin(2.0*(xd-C-1)/A))/np.pi;
ax1.plot(xd,hteor * n,'r')

dnl = val [xd]  / (hteor * n) - 1.0

ax2.plot(xd,dnl,'b')

ax2.set_xlabel('ADC code')
ax2.set_ylabel('DNL')
ax2.grid(True)
plt.show()
