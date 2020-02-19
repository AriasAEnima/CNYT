from ABC.libreriacomplejos import complejo as C
from ABC.libreriacomplejos import suma 
from ABC.libreriacomplejos import producto
from ABC.libreriacomplejos import resta
from ABC.libreriacomplejos import equals as eqc
class matrizcompleja:
    def __init__(self,mat=None):
        #self._mat=mat
        newmat=[]
        if not isinstance(mat[0][0], C):
            for i in mat:
                row=[]
                for j in i:               
                    row.append(C(j[0],j[1]))               
                newmat.append(row)
            self._mat=newmat
        else:
            self._mat=mat
        self._filas=len(self._mat)
        self._columnas=len(self._mat[0])

    def invmat(self):
        I=[]
        for i in range(self.filas):
            row=[]
            for j in range(self.columnas):
                row.append(producto(self.idx(i,j),C(-1,0)))
            I.append(row)
        return matrizcompleja(I)
   
    def trasmat(self):
        T=[]
        for i in range(self.columnas):
            row=[] 
            for j in range(self.filas):
                 row.append(self.idx(j,i))
            T.append(row)
        return matrizcompleja(T) 

    def conjmat(self):
        CO=[]
        for i in range(self.filas):
            row=[] 
            for j in range(self.columnas):
                 row.append(self.idx(i,j).conjugado())
            CO.append(row)
        return matrizcompleja(CO)

    def adjmat(self):
        ans=self.conjmat()  
        return ans.trasmat() 
    
    def norma(self):
        if self.columnas>1:
            raise Exception("ERROR: Debe ser un vector")
        return prodintmat(self,self).idx(0,0).a
    
    def unitaria(self):
        if(not self.cuadrada()):
            return False
        else:
            I=identidad(self.filas)
            ans=multmat(self.adjmat(),self)
            return equals(I,ans)
        
    def hermitiana(self):
        return equals(self,self.adjmat())        
    
    def cuadrada(self):
        return self.filas==self.columnas
    def potencia(self,n):
        if n==1:
            return self
        elif (n==0):
            return identidad(self.filas)
        else:
            if (n%2==0):
                return multmat(self.potencia(n//2),self.potencia(n//2))
            else:
                return multmat(multmat(self.potencia(n//2),self.potencia(n//2)),self)
    
    @property
    def mat(self):
        return self._mat
    
    @property
    def filas(self):
        return self._filas
                       
    @property
    def columnas(self):
        return self._columnas
    
    def __str__(self):
        string=""
        for i in self.mat:
            string+=str(i)+"\n"
        return string
    
    def idx(self,i,j):
        return self.mat[i][j]        
           
def summat(A,B):
    ans=[]
    if (A.filas!=B.filas or A.columnas!=B.columnas):
        raise Exception("ERROR: No comparten las dimensiones")
    for i in range(A.filas):
        row=[]
        for j in range(A.columnas):
            row.append(suma(A.idx(i,j),B.idx(i,j)))
        ans.append(row)
    return matrizcompleja(ans)

def multmat(A,B):
    ans=[]
    if (B.filas!=A.columnas):
        print(B.filas!=A.columnas," B y A : ", B.filas, A.columnas)
        raise Exception("ERROR: No comparten las dimensiones para lograr producto")
    for i in range(A.filas):
        row=[]        
        for j in range(B.columnas):
            sumando=C(0,0)
            for k in range(B.filas):
                #print("Indices A :{},{} Indices B {} ,{}".format(i,k,k,j))
                sumando=suma(sumando,producto(A.idx(i,k),B.idx(k,j)))                
            row.append(sumando)
        ans.append(row)
    return matrizcompleja(ans)

def accion(A,V):
    return multmat(A,V)

def multescmat(c,A):
    M=[]
    for i in range(A.filas):
        row=[] 
        for j in range(A.columnas):
            row.append(producto(A.idx(i,j),c))
        M.append(row)
    return matrizcompleja(M)

def prodintmat(V1,V2):
    return multmat(V1.adjmat(),V2)

def distanciavec(V1,V2):
    ans=[]
    if V1.columnas>1 or V2.columnas>1:
        raise Exception("ERROR: Algunos de los argumentos no es un vector")
    if V1.filas!=V2.filas:
        raise Exception("ERROR: No tienen la misma dimension")
    for i in range(V1.columnas):
        row=producto(V1.idx(i,0),V2.idx(i,0))
        ans.append(row)
    return matrizcompleja(ans)

def identidad(n):
    ans=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                row.append(C(1,0))
            else:
                row.append(C(0,0))
        ans.append(row)
    return matrizcompleja(ans)

def equals(V1,V2):
    if (V1.filas!=V2.filas or V1.columnas!=V2.columnas):
        return False
    for i in range(V1.filas):
        for j in range(V1.columnas):
            if (not eqc(V1.idx(i,j),V2.idx(i,j))):
                return False
    return True
def prodtensorial(A,B):
    ans=[]
    for i in range(A.filas*B.filas):
        row=[]
        for j in range(A.columnas*B.columnas):
            inA=A.idx(i//A.filas,j//A.columnas)
            inB=B.idx(i%B.filas,j%B.columnas)
            row.append(producto(inA,inB))
        ans.append(row)
    return ans
