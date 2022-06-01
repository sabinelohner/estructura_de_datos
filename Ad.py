class Ad:
    def __init__(self, code, c_name, location, title, type, desc):
        self.code=code
        self.c_name=c_name
        self.location=location
        self.title=title
        self.type=type
        self.desc=desc
    
    def lista(self):
        x=[self.code,self.type,self.title,self.desc,self.c_name,self.location]
        return x

    def generate_code(self):
        import random
        x=''
        for i in range(8):
            x=x+str(random.randint(0,9))
        self.code=x

    def get_code(self):
        return self.code
    
    def archivo_ad(self,x):
        import pickle
        if x[1]=='Fontanería':
            archivo=open('Solicitudes_Fontaneria','ab+')
            pickle.dump(x,archivo)
            archivo.close()
        elif x[1]=='Carpintería':
            archivo=open('Solicitudes_Carpinteria','ab+')
            pickle.dump(x,archivo)
            archivo.close()
        elif x[1]=='Electricidad':
            archivo=open('Solicitudes_Electricidad','ab+')
            pickle.dump(x,archivo)
            archivo.close()
        elif x[1]=='Jardinería':
            archivo=open('Solicitudes_Jardineria','ab+')
            pickle.dump(x,archivo)
            archivo.close()
        
    
    def get_code(self):
        return self.code
        
    def set_title(self,t):
        self.title=t

    def set_desc(self,d):
        self.desc=d
    
    def set_type(self,ty):
        
        if ty=='1':
            self.type="Fontanería"
        elif ty=='2':
            self.type="Carpintería"
        elif ty=='3':
            self.type="Electricidad"
        elif ty=='4':
            self.type="Jardinería"
    
    def get_cname(self):
        return self.c_name

    def get_title(self):
        return self.title

    def get_desc(self):
        return self.desc

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def hire_menu(self):
        self.title=input('Título de la publicación: ')
        print('Tipos de Servicios')
        x=input('''
1. Fontanería
2. Carpintería
3. Electricidad
4. Jardinería
>> ''')
        self.set_type(x)
        self.desc=input('Ingrese una breve descripción: ')
        self.location=input('Ingrese su ubicación: ')