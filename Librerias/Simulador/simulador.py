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
def resultado(D,I,clicks):
    print("Vector Estado final:")
    V=simulador(D,I,clicks)
    labels=label(I)
    estados=estado(V)
    index=np.arange(len(labels))
    plt.bar(index,estados)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index,labels,rotation=75)
    plt.title('Evolucion Dinamica del sistema despues de '+str(clicks)+' clicks')
    plt.show()
    print(estados)