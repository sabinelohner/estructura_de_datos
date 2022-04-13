#Sabine Lohner Villarroel
class Matriz:
    def __init__(self, filas, columnas):
        self.matriz=[]
        self.filas=filas
        self.columnas=columnas
    def llenarMatriz(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(int(input("[%d][%d]:"%(i+1,j+1))))
                print("-------------")
    def mostrarMatriz(self):
        for i in range(self.filas):
            print(self.matriz[i])
        print("--------------")
    def getMatriz(self):
        return self.matriz
    def setMatriz(self):
        self.matriz=matriz
    def paresMatriz(self,i):
        self.filas=(self.filas)+1
        self.matriz.append([])
        for j in range(self.columnas):
            x=0
            self.matriz[i].append(x+((j+1)*2))
    def getFilas(self):
        return self.filas
    def getColumnas(self):
        return self.columnas



fil=0
col=0
op=" "
while op!="0":
    print("Menu")
    print("1. Añadir un numero")
    print("2. Cargar los numeros pares")
    print("3. Mostrar la cantidad de elementos")
    print("0. Salir")
    op=input("Ingrese una opcion valida: ")
    if op=="1":
        fil=int(input("Digite el numero de filas: "))
        col=int(input("Digite el numero de columnas: "))
        m=Matriz(fil,col)
        m.llenarMatriz()
        m.mostrarMatriz()
    elif op=="2":
        m.paresMatriz(fil)
        m.mostrarMatriz()
    elif op=="3":
        f=m.getFilas()
        c=m.getColumnas()
        elementos=f*c
        print("Hay",elementos,"elementos")
    else:
        print("Ingrese una opción valida")
    