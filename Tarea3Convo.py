import numpy as np
import BinCon as bc

i,L=24,32 #Solución alternativa!

x=[-1.978, -2.884, 3.2431, -9.9132]
h=[-3.2566, 3.1432, -4.1654, 5.257, -4.6549]

print(bc.hexcon(bc.IE3(x)))
#conv=list(np.convolve(x,h))
#print(np.array(conv)-np.array(bc.invQi(bc.Qi(conv,2*i,2*L-1,1),2*i,1)))
#conv=list(np.convolve(x,h))
#conv=bc.Qi(conv,i,L,1)

#print(conv)
#print("Conv="+str(bc.hexcon(bc.Qi(conv,2*i,2*L-1,1))))
#print("Conv="+str(bc.invQi(bc.Qi(conv,2*i,2*L-1,1),2*i,1)))
#print("X="+str(bc.hexcon(bc.Qi(x,i,L,1))))
#print("H="+str(bc.hexcon(bc.Qi(h,i,L,1))))
#print(bc.IE3(2**127))
