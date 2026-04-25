class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever
print(dog.bark())  # Output: Woof!
    
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return "Meow!"

cat = Cat("Whiskers", "Orange")
print(cat.name)  # Output: Whiskers
print(cat.color)  # Output: Orange
print(cat.meow())  # Output: Meow!

class Person:
    company = "Tech Company"  # Class variable shared by all instances
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def get_age(self):
        return self.age
    def set_age(self, age):
        if age > 0 and age < 150 :
            self.age = age
        else:
            print("Invalid age")
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

        
person = Person("Mojidul", 25, "MT software company");
print(person.get_age());
person.set_age(34);
print(person.get_age());
print(person.set_age(-5)); # Invalid age
print(person.get_info());
print(Person.company); # Accessing class variable through class name
print(person.company); # Accessing class variable through instance

#object introspection
print(dir(person)) # List of all attributes and methods of the person object
    