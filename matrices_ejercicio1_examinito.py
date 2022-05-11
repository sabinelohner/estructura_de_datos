class Matriz:
    def __init__(self, filas, columnas):
        self.matriz=[]
        self.filas=filas
        self.columnas=columnas
    
    def matrizCero(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(None)
                
    def llenarMatriz(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==None:
                    z=int(input("Ingrese un número: "))
                    if z!=0:
                        self.matriz[i][j]=z
                    else:
                        break
                    if z==0 or self.isFull()==True:
                        break
                if z==0 or self.isFull()==True:
                        break
            if z==0 or self.isFull()==True:
                        break
                    
    def isFull(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==None:
                    return False
        return True
    
    def mostrarMatriz(self):
        for i in range(self.filas):
            print(self.matriz[i])
    
    def suma(self):
        suma=0
        for i in range(self.filas):
            for j in range(self.columnas):
                z=self.matriz[i][j]
                if z!=None:
                    suma=suma+z
        return suma
    
    def eliminarnumero(self,n):
        val=False
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j]==n:
                    self.matriz[i][j]=None
                    val=True
                if val==True:
                    break
            if val==True:
                break
        if val==False:
            print("El numero",n,"no está en la matriz")
            
    def lista(self,n):
        x=[]
        for i in range(self.filas):
            for j in range(self.columnas):
                t=self.matriz[i][j]
                if t==None:
                    t=0
                if t<n and t!=0:
                    x.append(self.matriz[i][j])
        return x
    
m=Matriz(3,3)
m.matrizCero()
m.mostrarMatriz()
#A
m.llenarMatriz()
m.mostrarMatriz()
#B
h=int(input("Ingrese un número: "))
m.eliminarnumero(h)
m.mostrarMatriz()
#C
s=m.suma()
print("La suma de los elementos es:",s)
#D
t=int(input("Ingrese un número: "))
x=m.lista(t)
print(x)
    