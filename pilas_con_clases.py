class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
s=Stack() #creando un objeto de la clase stack
print(s.isEmpty())
n=int(input("Ingrese cuantos numeros desea ingresar: "))
for i in range(n):
    x=int(input("Ingrese un numero: "))
    s.push(x)

for i in range(n):
    if s.isEmpty()==False:
        y=s.pop()     #Saca un valor
        print(y)
s.size()    #retorna el tamaño
