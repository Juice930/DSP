# -*- coding: utf-8 -*-
"""
hBgb4mzWQv9cY7qqVk05gmP0wCbRdV8hgzmC0pUq
"""

import numpy as np
import BinCon as bc
import matplotlib.pyplot as plt

N=[1,0,0]
D=[1,-0.4,-0.05]
h=bc.syntheticdivision(N,D,15)
np.set_printoptions(threshold=np.nan)
print(h)

a=[1,0.4,0.05]
print(bc.evaluate(a,15))

x=np.linspace(0,1000,1000)
Hanning=0.54-0.46*np.cos(2*np.pi*x/999)
Hamming=0.5-0.5*np.cos(2*np.pi*x/999)
plt.plot(Hanning)
plt.plot(Hamming)
