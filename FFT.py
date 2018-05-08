import numpy as np
import matplotlib.pyplot as plt
import BinCon as BC

fig, ax = plt.subplots(figsize=(20,10))
N=1024
x=np.linspace(0,N,N)
f1,f2=300,192
y1=np.cos(2*np.pi*f1*x/N)
y2=np.cos(2*np.pi*f2*x/N)
y=y1+y2
#plt.plot(y)
#plt.show()
h=BC.fft(y)
plt.plot(np.abs(h))
plt.axis([0,N,0,20])
plt.grid()
ax.minorticks_on()
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
