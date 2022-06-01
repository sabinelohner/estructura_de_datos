class W_Response:
    def __init__(self,w_name,w_categoria,w_score,code):
        self.nombre=w_name
        self.categoria=w_categoria
        self.score=w_score
        self.code=code

    def lista(self):
        x=[self.nombre,self.categoria,self.score,self.code]
        return x

    def respuesta_archivo(self):
        import pickle
        x=self.lista
        archivo=open('Respuestas_Trabajador','ab+')
        pickle.dump(x,archivo)
        archivo.close()

class C_Response:
    def __init__(self,code):
        self.code=code

    def cargar_respuestas(self):
        import pickle
        archivo=open('Respuestas_Trabajador','rb')
        lectura=True
        while lectura:
            try:
                data=pickle.load(archivo)
            except EOFError:
                lectura=False
            else:
                if data[-1]==self.code:
                    x=data
        archivo.close()
        return x