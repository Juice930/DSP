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
x=np.linspace(0,150,150)
y1=[1,1.95,1.9625,1.061375,0.107406,-0.084194,0.535587,1.290123,1.459074,0.924207,0.208306,-0.060697]
h1=bc.getEcenDif(y1)
y1=bc.evaluate(150,h1)

y2=[1,1.95,1.9625,1.061375,0.107406,-0.084194,0.535587]
h2=bc.getEcenDif(y2)
y2=bc.evaluate(150,h2)
plt.plot(y1,label='Modelo con 12 términos')
plt.plot(y2,'r',label='Modelo con 5 términos')
plt.legend(bbox_to_anchor=(0.5,0.9),loc=2,borderaxespad=0.)

raices=np.roots(h2[1:])
print(raices)
print(list(map(lambda n:np.abs(n),raices)))

"""
print(bc.convol(x,h))
print(bc.corr(x))
print(bc.corr(h))

print(np.correlate(x,x,"full"))
print(np.correlate(h,h,"full"))
"""