#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:07:48 2018

https://dzone.com/articles/sound-synthesis-numpy

@author: bernardo
"""

from numpy import linspace,sin,pi,int16
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
#from pylab import plot,show,axis

# tone synthesis
def note(freq, freq_mod, len, amp=1, rate=44100):
    mod_factor = 0.5
    t = linspace(0,len,len*rate)
    modul = sin(2*pi*freq_mod*t)
    modul = (1.0 + mod_factor * modul)/2.0
    data = sin(2*pi*freq*t)*amp * modul
    return data.astype(int16) # two byte integers



# A tone, 5 seconds, 44100 samples per second
tone = note(440, 20, 5,amp=32000)

write('440AMtone.wav',44100,tone) # writing the sound to a file

#plt.plot(linspace(0,2,2*44100),tone)

plt.plot(tone)
#axis([0,0.4,15000,-15000])
plt.show()