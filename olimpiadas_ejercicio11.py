a=input("Ingrese una palabra: ")

def es_palindromo(a):
    if a==a[::-1]:
        return True
    else:
        return False
    
print(es_palindromo(a))