frase=input("Introduzca una frase: ")
letra=input("Introduzca una letra: ")
c=0
for i in frase:
    if i == letra:
        c+=1

print("La letra",letra,"se repite ",c,"veces")