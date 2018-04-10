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
        
def __Qi(x,i,L,signed=0):#Convierte un solo número a arreglo binario
    sol=list()
    neg=False
    if abs(x)>2**(L-i): return 'error'
    if x<0:
        sol.append(0)
        neg=True
        x=-x
        L-=1
    elif signed!=0:
        sol.append(0)
        L-=1
    for k in range(L):
        if k<L-i:
            val=int(int(x)/(2**(L-i-k-1)))
            if val==2:
                sol[0]=1
                val=0
            sol.append(val)
            x=x%(2**(L-i-k-1))
        else:
            sol.append(int(x*2))
            x=2*x-sol[-1]
    if neg==True:
        return C2(sol)
    return sol

def invQi(num,i,signed=0):  #Convierte de arreglo o arreglos binarios a decimal
    if type(num[0])==list: return list(map(lambda n:__invQi(n,i,signed),num))
    else:               return __invQi(num,i,signed)
    
def __invQi(num,i,signed=0):#Sirve para un solo arreglo binario a decimal
    if(type(num)!=list): return 'error'
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
