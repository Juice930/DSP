import numpy as np
import BinCon as bc

i,L=24,32 #Solución alternativa!

x=[-1.978, -2.884, 3.2431, -9.9132]
h=[-3.2566, 3.1432, -4.1654, 5.257, -4.6549]
xbin=bc.Qi(x,11,16,1)
hbin=bc.Qi(h,11,16,1)

print(bc.hexcon(xbin))
print(bc.hexcon(hbin))

x2=bc.invQi(xbin,11,1)
h2=bc.invQi(hbin,11,1)
corr=bc.Qi(bc.corr(x2,h2),21,31,1)

print(bc.hexcon(corr))
print(np.array(bc.invQi(corr,21,1)))
print(np.correlate(x,h,"full"))
print(np.array(bc.invQi(corr,21,1))-np.correlate(x,h,"full"))#Error
#print(bc.invQi(xbin,11,1))
#print(bc.invQi(hbin,11,1))

"""
x=[1,2,1,1]
h=[1,1,2,1]
print(bc.corr(x))
print(bc.corr(h))

print(np.correlate(x,x,"full"))
print(np.correlate(h,h,"full"))
"""