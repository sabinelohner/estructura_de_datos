class Help:
    def __init__(self,name,user_type,text):
        self.name=name
        self.user_type=user_type
        self.text=text

    def lista(self):
        x=[self.name,self.user_type,self.text]
        return x

    def archivo(self):
        import pickle
        x=self.lista()
        arch=open('Ayuda','ab+')
        pickle.dump(x,arch)
        arch.close()