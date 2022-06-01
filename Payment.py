class Payment:
    def __init__(self, code, w_name, pay):
        self.code=code
        self.w_name=w_name
        self.pay=pay
        self.fecha=''
        self.comision=10
    
    def lista(self):
        x=[self.code,self.w_name,self.fecha,self.pay,self.comision]
        return x
        
    def archivos(self):
        import pickle
        x=self.lista
        archivo=open('Pagos','ab+')
        pickle.dump(x,archivo)
        archivo.close()
        

    def set_date(self):
        from datetime import date
        today=date.today()
        f=today.strftime("%d/%m/%Y")
        self.fecha=f

    def set_pay(self,x):
        self.pay=x
        
    def get_pay(self):
        return self.pay
        
    def ganancia(self):
        g=10+((int(self.pay)-50)*0.1)
        round(g,2)
        self.comision=str(g)

    def importar(self):
        import pickle
        archivo=open('Pagos','rb')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                print(data)
        archivo.close()

    def ganancia_total(self):
        x=[]
        import pickle
        archivo=open('Pagos','rb')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                x.append(float(data[3]))
        archivo.close()
        g=0
        for i in range(len(x)):
            g=g+x[i]
        return g
