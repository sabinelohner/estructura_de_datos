dias=[]
dias2=[]
dias.append("lunes")
dias.append("martes")
dias.append("miercoles")
dias.append("jueves")
dias.append("viernes")
dias.append("sabado")
dias.append("domingo")
for i in range(7):
    x=dias.pop()
    dias2.append(x)
print(dias2)