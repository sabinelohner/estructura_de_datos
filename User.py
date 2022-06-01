
class Client:
    def __init__(self,nombre,contrasena,sexo,edad,mail,telefono):
        self.nombre=nombre
        self.contrasena=contrasena
        self.sexo=sexo
        self.edad=edad
        self.mail=mail
        self.telefono=telefono


    def lista(self):
        x=[self.nombre,self.contrasena,self.sexo,self.edad,self.mail,self.telefono]
        return x
    
    def registro(self):
        name=input('Nombre: ')
        apellidoP=input('Apellido Paterno: ')
        apellidoM=input('Apellido Materno: ')
        self.nombre=f'{name} {apellidoP} {apellidoM}'
        date=input('Fecha de nacimiento (dd/mm/aaaa): ')
        self.edad=date
        sex=input('Sexo (M/F): ')
        self.sexo=sex
        telf=input('Teléfono: ')
        self.telefono=telf
        correo=input('Correo electrónico: ')
        self.mail=correo
        pas=input('Contraseña: ')
        self.contrasena=pas

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