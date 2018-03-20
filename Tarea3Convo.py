#import numpy as np
import BinCon as bc

i,L=20,32 #Solución alternativa!

x=[-1.978, -2.884, 3.2431, -9.9132]
h=[-3.2566, 3.1432, -4.1654, 5.257, -4.6549]

conv=bc.convol(x,h)
conv=bc.Qi(conv,i,L,1)
"""
print(conv)
print(bc.invQi(conv,i,1))
print(np.convolve(x,h))
"""
print(bc.IE3(x))
print(bc.InvIE3(bc.IE3(x)))
print(bc.IE3(2**127))
print(bc.InvIE3(bc.IE3(2**127)))

"""
for j in range(-32,32):
    print(j,bc.Qi(j,0,6,1),bc.C2(bc.Qi(j,0,6,1)))
"""