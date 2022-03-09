lista=input("Introduce números separados por comas: ")
lista=lista.split(',')
suma=0
sumasq=0
for i in lista:
    suma=suma+int(i)
    sumasq+=int(i)**2

n=len(lista)
p=suma/n
stdev=(sumasq/n-p**2)**(1/2)
print("La media es",p,"y la desviación típica es",stdev)