class C_Verification:
    def __init__(self,mail,password):
        self.mail=mail
        self.password=password

    def verificacion(self):
        import pickle
        import time
        archivo=open('Clientes','rb')
        cliente=None
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=True
            else:
                if data[1]==self.password and data[4]==self.mail:
                    cliente=data
        if cliente!=None:
            return cliente
        else:
            print('Error en el registro \nVerifique si ya tiene una cuenta o sus credenciales son correctos')
            time.sleep(3)


class W_Verification:
    def __init__(self,mail,password):
        self.mail=mail
        self.password=password 

    def verificacion(self,mail,password):
        import pickle
        import time
        archivo=open('Trabajadores','rb')
        trabajador=None
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=True
            else:
                if data[1]==password and data[4]==mail:
                    trabajador=data
        if trabajador!=None:
            return trabajador
        else:
            print('Error en el registro \nVerifique si ya tiene una cuenta o sus credenciales son correctos')
            time.sleep(3)

