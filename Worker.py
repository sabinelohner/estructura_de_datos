class Worker:
    def __init__(self,nombre,contrasena,sexo,dni,edad,mail,telefono):
        self.nombre = nombre
        self.contrasena=contrasena
        self.sexo=sexo
        self.dni= dni
        self.edad= edad
        self.mail=mail
        self.telefono=telefono


    def lista(self):
        x=[self.nombre,self.contrasena,self.sexo,self.edad,self.mail,self.telefono,self.dni]
        return x

    def registro(self):
            name=input('Nombre: ')
            apellidoP=input('Apellido: ')
            apellidoM=input('Apellido: ')
            self.nombre=f'{name} {apellidoP} {apellidoM}'
            date=input('Fecha de nacimiento (dd/mm/aaaa): ')
            self.edad=date
            sex=input('Sexo (M/F): ')
            self.sexo=sex
            telf=input('Teléfono: ')
            self.telefono=telf
            ci=input('C.I.: ')
            self.dni=ci
            correo=input('Correo electrónico: ')
            self.mail=correo
            pas=input('Contraseña: ')
            self.contrasena=pas


# ---------------------------------------------------

    def get_nombre (self):
        return self.nombre

    def get_contrasena(self):
        return self.contrasena
    
    def get_sexo(self):
        return self.sexo

    def get_dni(self):
        return self.dni

    def get_edad(self):
        return self.edad

    def get_mail(self):
        return self.mail

    def get_telefono(self):
        return self.telefono