import os

class C_Profile:
    
    def __init__(self,nombre,contrasena,sexo,edad,mail,telefono,ubicacion):
        self.nombre=nombre
        self.contrasena=contrasena
        self.sexo=sexo
        self.edad=edad
        self.mail=mail
        self.telefono=telefono
        self.ubicacion=ubicacion

        
    def todo_lista(self):
        x=[self.nombre,self.contrasena,self.sexo,self.edad,self.mail,self.telefono,self.ubicacion]
        return x

    def perfil(self):
        print(self.nombre)
        print(f'Sexo: {self.sexo}')
        print(f'Fecha de nacimiento: {self.edad}')
        print(f'Telefono: {self.telefono}')
        print(f'Mail: {self.mail}')
        print(f'Ubicaciones: {self.ubicacion}')
    
    
    def archivos(self):
        import pickle
        archivo=open('Clientes','ab+')
        x=self.todo_lista()
        pickle.dump(x,archivo)
        archivo.close


    def get_Ubicacion(self):
        return self.ubicacion
    
    def set_Ubicacion(self,x):
        self.ubicacion=x

    def get_Nombre(self):
        return self.nombre
    
    def get_Contrasena(self):
        return self.contrasena
    
    def get_Sexo(self):
        return self.sexo
    
    def get_Edad(self):
        return self.edad
    
    def get_Mail(self):
        return self.mail
    
    def get_Telefono(self):
        return self.telefono