class Student():
    def __init__(self,value):
        self.id = value
        self.fname = None
        self.sname = None
        self._age = 0
        
    def show(self,idF=0):
        listAntibuit = [self.id,self.fname,self.sname,self._age]
        print(listAntibuit[idF])
    
    def print(self):
        print([self.id,self.fname,self.sname,self._age])
        
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        