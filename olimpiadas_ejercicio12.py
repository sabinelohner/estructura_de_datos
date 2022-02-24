class Rectangulo:
    def _init_(self,b,h):
        self.b=b
        self.h=h
        
    def area(self):
        return self.b*self.h
    
rectangulo=Rectangulo(20,10)
print("Área del rectángulo: ",rectangulo.area())