# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:02:42 2018

@author: Guillermo1
"""

import numpy as np
import matplotlib.pyplot as plt
import BinCon as BC
f1=BC.osc(2*np.pi*3/32,32)
f2=BC.osc(2*np.pi*100/32,32)
plt.plot(f1)
plt.plot(f2)
plt.show()
plt.plot(f1*f2)
plt.show()
plt.plot(BC.FFT(f1*f2))

N_min = min(32, 32)
n = np.arange(N_min)
k = n[:, None]
M = np.exp(-2j * np.pi * n * k / N_min)
X = np.dot(M, (f1*f2).reshape((N_min, -1)))#M por x transpuesta
help(np.fft.fft())