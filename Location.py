class Location:
    def __init__(self):
        self.ubicaciones=[]
        
    def add_location(self,x):
        self.ubicaciones.append(x)
        
    def get_location(self):
        return self.ubicaciones