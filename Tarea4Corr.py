import numpy as np
import BinCon as bc
import matplotlib.pyplot as plt

i,L=24,32 #Solución alternativa!
"""
x=[-1.978, -2.884, 3.2431, -9.9132]
h=[-3.2566, 3.1432, -4.1654, 5.257, -4.6549]
xbin=bc.Qi(x,11,16,1)
hbin=bc.Qi(h,12,16,1)

print(bc.hexcon(xbin))
print(bc.hexcon(hbin))

x2=bc.invQi(xbin,11,1)
h2=bc.invQi(hbin,12,1)
corr=bc.Qi(bc.corr(x2,h2),23,31,1)

print(bc.hexcon(corr))
print(np.array(bc.invQi(corr,23,1)))
print(np.correlate(x,h,"full"))
print(np.correlate(x,h,"full")-np.array(bc.invQi(corr,23,1)))#Error
"""
#print(bc.invQi(xbin,11,1))
#print(bc.invQi(hbin,11,1))
N = [1,0,0]
D = [1,-0.4,-0.05]

x=[1,2,1,1]
h=[1,1,2,1]
#print(bc.syntheticdivision(N,D,11))
y1=[1,1.95,1.9625,1.084375,0.152256,-0.039056,0.560527,1.293624,1.458176,0.937099,0.238059,-0.027158,0.301328,0.838841,1.058334]
h1=bc.getEcenDif(y1)
y1=bc.evaluate(h1,150)

y2=[1,1.95,1.9625,1.084375,0.152256,-0.039056,0.560527,1.293624,1.458176,0.937099,0.238059,-0.027158,0.301328,0.838841,1.058334]
h2=bc.getEcenDif(y2)
y2=bc.evaluate(h2,150)
plt.plot(y1,label='Modelo con 12 términos')
plt.plot(y2,'r',label='Modelo con 5 términos')
plt.legend(bbox_to_anchor=(0.5,0.9),loc=2,borderaxespad=0.)
plt.show()
Hchida=[1.00000000e+00,   1.95000000e+00,  -1.84000000e+00,8.45500000e-01]
plt.plot(bc.evaluate(Hchida,100))
raices=np.roots([-1]+Hchida[1:])
print(raices)
"""
print(bc.convol(x,h))
print(bc.corr(x))
print(bc.corr(h))

print(np.correlate(x,x,"full"))
print(np.correlate(h,h,"full"))
"""