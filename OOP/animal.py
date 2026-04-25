from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass 

class Dog(Animal):
    def sound(self):
        return "Bark"

# animal = Animal() # This will raise an error because we cannot instantiate an abstract class
dog = Dog()
print(dog.sound())