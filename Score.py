class Score:
    def __init__(self,name,type,score):
        self.name=name
        self.type=type
        self.score=score

    def lista(self):
        x=[self.name,self.type,self.score]
        
    def get_score(self):
        return self.score
        
    def set_score(self,x):
        self.score=x

    def conjunto(self):
        y=[]
        x=self.lista()
        y.append(x)
        return y