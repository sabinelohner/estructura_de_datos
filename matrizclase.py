class Matriz:
    #constructor y atributos de la clase Matriz
    def __init__(self, filas, columnas):
        self.matriz=[]
        self.filas= filas
        self.columnas= columnas


    #m?todo que llena la matriz
    def llenarMatriz(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                self.matriz[i].append(int(input("[%d][%d]: "%(i+1,j+1))))
                print ("-----------")


    #m?todo que muestra la matriz
    def mostrarMatriz(self):
        for i in range(self.filas):
            print(self.matriz[i])
        print ("-----------")

    #m?todo que devuelve la matriz del objeto matriz
    #(la clase Matriz tiene una matriz como atributo)
 
    def getMatriz(self):
        return self.matriz

    #m?todo que devuelve el numero de filas de la matriz
    def getFilas(self):
        return self.filas

    #m?todo que devuelve el numero de columnas de la matriz
    def getColumnas(self):
        return self.columnas

    #m?todo que recibe como par?metro una matriz que modificar? a la matriz
    #del objeto
    def setMatriz (self, matriz):
        self.matriz= matriz
    
    #sumarMatriz
    def sumarMatriz(self, matrizB):
        matrizRes= []
        for i in range(self.filas):
            list_a = []
            for j in range(matrizB.columnas):
                mult=self.matriz[i][j]+matrizB.matriz[i][j]
                list_a.append(mult)
            matrizRes.append(list_a)
        return matrizRes
                #print(list_a)
                
    #metodo que multiplica dos matrices
    def multiplicarMatriz(self, matrizB):

        if self.columnas!= matrizB.filas:
            print("Las matrices seleccionadas no pueden multiplicarse...")
        else:
            matrizRes= []
            for i in range(self.filas):
                list_a = []
                for j in range(matrizB.columnas):
                    mult= 0
                    for k in range(matrizB.filas):
                        mult+=self.matriz[i][k]*matrizB.matriz[k][j]
                    list_a.append(mult)
                matrizRes.append(list_a)
                #print(list_a)

        return matrizRes
    
    def matrizTraspuesta(self):
        matrizRes=[]
        for i in range(self.columnas):
            list_a=[]
            for j in range(self.filas):
                k=self.matriz[j][i]
                list_a.append(k)
            matrizRes.append(list_a)
        return matrizRes
            


filA=int(input("Digite el numero de filas: \n"))
colA=int(input("Digite el numero de columnas: \n"))
matrizA= Matriz(filA , colA)
colB=0
filB=0
op=" "
while op!="s" and op!="S":
    print ("------------------------------------------")
    print("\t\tMENU\t\t")
    print("(C)argar matriz")
    print("s(U)mar matriz")
    print("(M)ultiplicar matriz")
    print("(T)raspuesta")
    print("(S)alir")
    print("NOTA: para multiplicar matrices primero debe cargar la matriz")
    op= input("Ingrese una opcion valida: ")

    if op=="c" or op=="C":

        matrizA.llenarMatriz()
    elif op=="u" or op=="U":
            matrizB= Matriz(filA , colA)
            matrizB.llenarMatriz()

            matrizC= Matriz(filA , colB)
            matrizResultado= matrizA.sumarMatriz(matrizB)
            matrizC.setMatriz(matrizResultado)
            matrizC.mostrarMatriz()

    elif op=="m" or op=="M":

            filB=int(input("Digite el numero de filas de la segunda matriz: \n"))
            colB=int(input("Digite el numero de columnas de la segunda matriz: \n"))
            matrizB= Matriz(filB , colB)
            matrizB.llenarMatriz()

            matrizC= Matriz(filA , colB)
            matrizResultado= matrizA.multiplicarMatriz(matrizB)
            matrizC.setMatriz(matrizResultado)
            matrizC.mostrarMatriz()
    
    elif op=="t" or op=="T":
        
        matrizC= Matriz(filA , colA)
        matrizResultado=matrizA.matrizTraspuesta()
        matrizC.setMatriz(matrizResultado)
        matrizC.mostrarMatriz()
    
    else:
        print("Digite una opcion valida \n")


exit(0)