class C_Records:
    def __init__(self, code, type, c_name, w_name, pay, score):
        self.code=code
        self.type=type
        self.c_name=c_name
        self.w_name=w_name
        self.payment=pay
        self.score=score

    def lista(self):
        x=[self.code,self.type,self.c_name,self.w_name,self.payment,self.score]
        return x

    def guardar(self):
        import pickle
        x=self.lista()
        archivo=open('Historial_TrabajosTerminados','ab+')
        pickle.dump(x,archivo)
        archivo.close()

class W_Records:
    def __init__(self):
        self.conjunto=[]

    def historial(self,name,category):
        import pickle
        archivo=open('Historial_TrabajosTerminados','rb')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                if data[3]==name and data[1]==category:
                    self.conjunto.append(data)
        archivo.close()
        for i in range(len(self.conjunto)):
            print(self.conjunto[i])