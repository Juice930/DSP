import BinCon as BC
import numpy as np
np.set_printoptions(threshold=np.inf)
x=[2.398, -3.8778, 4.1231, -3.19402, 0.88986, -6.349152, -2.16793, 9.568]
h=[1.1257, -2.4563, 5.66754, -3.257, 6.7654, 3.3241, 2.3987, 0.9876]
print(np.convolve(x,h,mode='full'))
x=BC.Qi(x,27,32,1)
x=BC.invQi(x,27,1)
print(x)
