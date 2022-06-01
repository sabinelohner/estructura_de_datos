class Job_IP:
    def __init__(self, code, type, c_name, w_name, state):
        self.code=code
        self.type=type
        self.c_name=c_name
        self.w_name=w_name
        self.state=state
        
    def lista(self):
        x=[self.code,self.type,self.c_name,self.w_name,self.state]
        return x
        
    def generate_code(self):
        import random
        x=''
        for i in range(8):
            x=x+str(random.randint(0,9))
        return x
    
    def archivos(self,x):
        import pickle
        x=self.lista
        archivo=open('Trabajos_En_Proceso','ab+')
        pickle.dump(x,archivo)
        archivo.close()

    def comunicacion(self):
        import pickle
        archivo=open('Trabajos_En_Proceso','rb+')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                if self.code==data[0]:
                    trabajo=data
        archivo.close()
        return trabajo

    def actualizar(self):
        import pickle
        import os
        x=[]
        archivo=open('Trabajos_En_Proceso','rb+')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                x.append(data)
        archivo.close()
        aux=open('temp','ab+')
        for i in range(len(x)):
            if x[i][0]!=self.code:
                pickle.dump(x[i],aux)
        z=self.lista()
        pickle.dump(z,aux)
        aux.close()
        os.remove('Trabajos_En_Proceso')
        os.rename('temp','Trabajos_En_Proceso')
        

    def get_c_name(self):
        return self.c_name


    def get_w_name(self):
        return self.w_name

    def get_code(self):
        return self.code

    def set_code(self,x):
        self.code=x
        
    def set_state(self,x):
        self.state=x
    
    def get_state(self):
        return self.state

    def get_type(self):
        return self.type

    def state_cliente(self):
        if self.get_state()=='0':
            print('Has aceptado la respuesta de un trabajador')
        elif self.get_state()=='1':
            print('El trabajador está en camino')
        elif self.get_state()=='2':
            print('El trabajador ha llegado a destino')
        elif self.get_state()=='3':
            print('El trabajo está siendo realizado')
        elif self.get_state()=='4':
            print('Trabajo finalizado') 