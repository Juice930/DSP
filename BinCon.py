#Convolución Discreta con herramientas de conversión binaria
#Juice930
#artvel_0412@hotmail.com
import numpy as np
def C1(x): #Complemento a 1
    return list(map(lambda n:n^1,x))

def C2(x):
    if type(x[0])==list:   return list(map(lambda n:__C2(n),x))
    else:               return __C2(x)
def __C2(x): #Complemento a 2 
    if not (1 in x):
        return [0]*len(x)
    x=C1(x)
    x.reverse()
    for i,j in enumerate(x):
        x[i]^=1
        if x[i]==1:
            break        
    x.reverse()
    return x
def hexcon(x):
    if type(x[0])==list:   return list(map(lambda n:hex(int(__bincon(n)[2:],2)),x))
    else:               return hex(int(__bincon(x)[2:],2))
def bincon(x):
    if type(x[0])==list:   return list(map(lambda n:__bincon(n),x))
    else:               return __bincon(x)
def __bincon(x):
    res=str()
    for i in x:
        res+=str(i)
    return bin(int(res,2))
def IE3(x):
    if type(x)==list:   return list(map(lambda n:__IE3(n),x))
    else:               return __IE3(x)
    
def __IE3(num):
    if num==0 or abs(num)<2**-126:
        return [0]*32
    elif num>2**128-1:
        return [0]+[1 for i in range(31)]
    elif num<-2**128-1:
        return [1]+[1 for i in range(31)]
    s=0
    if num<0:
        s=1
        num=-num
    if 0<=num<2**64:
        L=int(np.log2(num)+1)
        exp=Qi(int(127+np.log2(num)),0,8)        
    else:
        L=64+int(np.log2(num/(2**64))+1)
        exp=Qi(int(127+64+np.log2(num/2**64)),0,8)
        
    if L>=1:    
        aux=Qi(num*2**-L,24,24)[1::]
    else:
        aux=Qi(num*2**(-L-1),24,24)[1::]
    return [s]+exp+aux

def InvIE3(arr):
    if type(arr[0])==list:  return list(map(lambda n:__InvIE3(n),arr))
    else:                   return __InvIE3(arr)
    
def __InvIE3(arr):
    exp=invQi(arr[1:9],0)-127
    mant=invQi([1]+arr[9::],23)
    return ((-1)**arr[0])*(2**exp)*mant

def Qi(x,i,L,signed=0): #Convertir número o números de decimal a arreglo binario
    if type(x)==list:   return list(map(lambda n:__Qi(n,i,L,signed),x))
    else:               return __Qi(x,i,L,signed=0)

def __Qi(x,i,L,signed=0):
    if abs(x)>2**(L-i) and L>i and i<0: return 'error'
    res=bin(int(x*2**i))
    Long=len(res[res.find('b')+1:])
    if res[0]=='-':
        return [1]*(L-Long)+C2([int(i) for i in res[res.find('b')+1:]])
    elif signed!=0:
        return [0]*(L-Long)+list([int(i) for i in res[res.find('b')+1:]])
    return [0]*(L-Long)+list([int(i) for i in res[res.find('b')+1:]])    

def invQi(num,i,signed=0):  #Convierte de arreglo o arreglos binarios a decimal
    if type(num[0])==list: return list(map(lambda n:__invQi(n,i,signed),num))
    else:               return __invQi(num,i,signed)
def __invQi(num,i,signed=0):#Sirve para un solo arreglo binario a decimal
    if(type(num)!=list): return 'error'
    #TODO:Checar con el signado!!!
    if signed!=0:
        if num[0]==1:
            num=C2(num)
            return -sum([k*(2**(len(num)-i-j-1)) for j,k in enumerate(num)])
        else:
            return sum([k*(2**(len(num)-i-j-1)) for j,k in enumerate(num)])
    return sum([k*(2**(len(num)-i-j-1)) for j,k in enumerate(num)])

def convol(x,y):            #Convolución discreta de dos arreglos
    res=[0]*(len(x)+len(y)-1)
    for n in range(len(res)):
        for k in range(n+1):
            try:
                res[n]+=x[k]*y[n-k]
            except:
                res[n]+=0
    return res

def corr(x,y=[]):           #Correlación o Autocorrelación
    if y==[]:               #Si solo se dio un argumento se asume autocorrelación
        return convol(x,x[::-1])
    return convol(x,y[::-1])
 
def syntheticdivision(dividend, divisor,it):    #Código adaptado a nuestras necesidades
    '''Fast polynomial division by using Extended Synthetic Division. Also works with non-monic polynomials.'''
    # dividend and divisor are both polynomials, which are here simply lists of coefficients. Eg: x^2 + 3x + 5 will be represented as [1, 3, 5]
    h = []
    out = list(dividend) # Copy the dividend
    normalizer = divisor[0]
    for k in range(it-1):
        for i in range(len(dividend)-(len(divisor)-1)):
            out[i] /= normalizer
            coef = out[i]
            if coef != 0:
                for j in range(1, len(divisor)):
                    out[i + j] += -divisor[j] * coef
        separator = -(len(divisor)-1)
        h.append(out[:separator][0]*(-1)**k)
        out=list(map(lambda n:-n,out[separator:]))+[0]
    return np.array(h)

def getEcenDif(y):
    h=[y[0]]
    for i in range(1,len(y)):
        h.append(y[i]-sum([y[j]*h[-j] for j in range(1,i)]))
    return np.array(h)

def evaluate(it,a):
    h=[a[0]]
    for i in range(1,len(a)):
        h.append(sum([a[j]*h[-j] for j in range(1,i+1)]))
    for i in range(len(a),it):
        h.append(sum([a[j]*h[-j] for j in range(1,len(a))]))
    return np.array(h)

def Wkn(k,N=32):
    return np.exp(-2j*np.pi*k/N)

def rev(a):
    a.reverse()
    return a

def indix(N):
    L=int(np.log2(N)-1)
    index=[]
    for i in range(N//2):
        index.append(invQi(rev(Qi(i,0,L)),0))
    return index,L

def __fft(h,N,radix):
    y=h.copy()
    for i in range(0,N,2*radix):
        for j in range(radix):
            y[i+j]+=h[i+j+radix]*Wkn(j*N//(2*radix),N)
            y[i+j+radix]=h[i+j]-h[i+j+radix]*Wkn(j*N//(2*radix),N)
    return y

def fft(h):
    N=len(h)
    index,L=indix(N)
    y=h.copy()
    h=[]
    for i in index:
        h.append(y[i]+y[i+N//2])
        h.append(y[i]-y[i+N//2])
    print("Iteración número 0")
    for i,j in list(enumerate(h)):
        print(i,j)
    for i in range(1,L+1):
        h=__fft(h,N,2**i)
        print("Iteración número "+str(i))
        for j,k in list(enumerate(h)):
            print(j.k)
        
    return h
