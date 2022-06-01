class W_Profile:
    def __init__(self,nombre,contrasena,sexo,dni,edad,mail,telefono,type,calificacion):
        self.nombre = nombre
        self.contrasena=contrasena
        self.sexo=sexo
        self.dni= dni
        self.edad= edad
        self.mail=mail
        self.telefono=telefono
        self.categoria=type
        self.score=calificacion

# ---------------------------------------------------
    def lista(self):
        x= [self.nombre,self.contrasena,self.dni,self.edad,self.sexo,self.telefono,self.mail,self.categoria,self.score]
        return x

    def archivos(self):
        import pickle
        archivo=open('Trabajadores','ab+')
        x=self.lista()
        pickle.dump(x,archivo)
        archivo.close
    

    def perfil(self):
        print(self.nombre)
        print(f'Área de especialidad: {self.categoria}')
        print(f'Calificación: {self.score}')
        print(f'Sexo: {self.sexo}')
        print(f'Fecha de nacimiento: {self.edad}')
        print(f'Telefono: {self.telefono}')
        print(f'Mail: {self.mail}')

#---------------------------------------------
    def get_telefono(self):
        return self.telefono
    def set_telefono(self,telefono):
        self.telefono = telefono
#--------------------------------------------
    def get_nombre (self):
        return self.nombre
    def set_nombre (self,nombre):
        self.nombre = nombre
#-------------------------------------------
    def get_contraseña(self):
        return self.contrasena
    def set_contrasena(self,contrasena):
        self.contrasena = contrasena
        
    def getdni(self):
        return self.dni
    def setdni(self,dni):
        self.dni=dni
#-----------------------------------------
    def getedad(self):
        return self.edad
    def setedad(self,edad):
        self.edad=edad

    def get_categoria(self):
        return self.categoria

    def get_score(self):
        return self.score