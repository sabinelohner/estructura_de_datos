class Browsing_Page():
    def __init__(self,type):
        self.browse=[]
        self.type=type

    def import_ads(self):
        import pickle
        if self.type=='Fontanería':
            archivo=open('Solicitudes_Fontaneria','rb')
            lectura=True
            while lectura:
                try:
                    data=pickle.load(archivo)
                except EOFError:
                    lectura=False
                else:
                    self.browse.append(data)
        elif self.type=='Carpintería':
            archivo=open('Solicitudes_Carpinteria','rb')
            lectura=True
            while lectura:
                try:
                    data=pickle.load(archivo)
                except EOFError:
                    lectura=False
                else:
                    self.browse.append(data)
        elif self.type=='Electricidad':
            archivo=open('Solicitudes_Electricidad','rb')
            lectura=True
            while lectura:
                try:
                    data=pickle.load(archivo)
                except EOFError:
                    lectura=False
                else:
                    self.browse.append(data)
        elif self.type=='Jardinería':
            archivo=open('Solicitudes_Jardineria','rb')
            lectura=True
            while lectura:
                try:
                    data=pickle.load(archivo)
                except EOFError:
                    lectura=False
                else:
                    self.browse.append(data)

    def show_ads(self):
        if len(self.browse)==0:
            print('No hay solicitudes en este momento. Vuelva a intentarlo más tarde')
        else:
            for i in range(len(self.browse)):
                print(f'{i+1}. {self.browse[i]}')
    
    def select_ad(self):
        import pickle
        import os
        x=input('Seleccione una solicitud: ')
        solicitud=self.browse[x+1]
        self.browse[x+1]=None
        aux=open('temp','ab+')
        for i in range(self.browse):
            if self.browse[i]!=None:
                pickle.dump(self.browse[i],aux)
        aux.close()
        if self.type=='Fontanería':
            os.remove('Solicitudes_Fontaneria')
            os.rename('temp','Solicitudes_Fontaneria')
        elif self.type=='Carpintería':
            os.remove('Solicitudes_Carpinteria')
            os.rename('temp','Solicitudes_Carpinteria')
        elif self.type=='Electricidad':
            os.remove('Solicitudes_Electricidad')
            os.rename('temp','Solicitudes_Electricidad')
        elif self.type=='Jardinería':
            os.remove('Solicitudes_Jardineria')
            os.rename('temp','Solicitudes_Jardineria')
        return solicitud