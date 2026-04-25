class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the parent class
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the constructor of the parent class
        self.color = color

    def speak(self):
        return "Meow!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.speak())  # Output: Woof!
cat = Cat("Whiskers", "Orange")
print(cat.name)  # Output: Whiskers
print(cat.color)  # Output: Orange
print(cat.speak())  # Output: Meow!