class Job_Title:
    def __init__(self,categoria,certificacion):
        self.categoria = categoria
        self.certificacion= certificacion

# ---------------------------------------------------
    def lista(self):
        x= [self.categoria,self.certificacion]
        return x

#---------------------------------------------
    def get_categoria(self):
        return self.categoria
    def set_categoria(self,x):
        if x=='1':
            self.categoria='Fontanería'
        elif x=='2':
            self.categoria='Carpintería'
        elif x=='3':
            self.categoria='Electricidad'
        elif x=='4':
            self.categoria='Jardinería'

#--------------------------------------------
    def get_certificacion (self):
        return self.certificacion
    def set_certificacion (self,certificacion):
        if certificacion=='1':
            self.certificacion='Certificación: Sí'
        elif certificacion=='2':
            self.certificacion='Certificación: No'

        
