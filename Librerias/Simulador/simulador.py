import numpy as np 
import matplotlib.pyplot as plt
from Matriz_Compleja.libreriamatrices import matrizcompleja as mc
from Matriz_Compleja.libreriamatrices import multmat as mult
from Matriz_Compleja.libreriamatrices import prodtensorial as tens

def simulador(D,I,n):
    return mult(D.potencia(n),I)

def label(I):
    ans=[]
    for i in range(I.filas):
       ans.append("Pto "+str(i))
    return ans
def estado(V):
    ans=[]
    for i in range(V.filas):
       ans.append(V.idx(i,0).a)
    return ans
def resultado(D,I,clicks,labels=None,fs=None,v2s=None,L1=None,L2=None):
    print("Vector Estado final:")
    V=simulador(D,I,clicks)  
    if (labels==None and fs!=None):
        labels=generateLabels(fs,v2s,L1,L2)
    else:
        labels=label(I)
    estados=estado(V)
    index=np.arange(len(labels))
    plt.bar(index,estados)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index,labels,rotation=90)
    plt.title('Evolucion Dinamica del sistema despues de '+str(clicks)+' clicks')
    plt.show()
    return estados

def generateLabels(fs,v2s,L1,L2):
    a=[]
    for i in range(fs):
        a.append(str(L1)+" : "+str(i//v2s)+" , "+str(L2)+" : "+str(i%v2s))
    return a

def addLabels(labels,fs,v2s,L):
    a=[]
    for i in range(fs):
        a.append(labels[i//v2s]+" , "+str(L)+" : "+str(i%v2s))
    return a
            