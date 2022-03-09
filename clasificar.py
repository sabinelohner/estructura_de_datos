a = []
n=int(input("¿Cuántos números desea ingresar?: "))
for i in range(n):
    a.append(int(input("Introduce un número: ")))
a.sort()
print("Números ganadores: ",a)
    