class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
#add deleter
    @name.deleter
    def name(self):
        del self._name
        
p = Person("Mojidul")
print(p.name)
p.name = "Nayeem"
print(p.name)
del p.name
print(p.name)