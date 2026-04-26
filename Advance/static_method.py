class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    #instance method
    def get_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
       
    @staticmethod # if this decorator is missing shows an error
    def sum(a, b):
        return a+b      
             
employee = Employee("Mojidul", 120000)
employee.get_info()
sm = employee.sum(2,56)
print(sm)

#classmethod example
class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    #instance method
    def get_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    
    #can also be called by class name without creating an instance of the class
    #can be used to create an instance of the class using a string
    #if this decorator is missing shows an error don't need to use self or cls as parameter
    @staticmethod
    def sum(a, b):
        return a+b
    
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

employee = Employee("Mojidul", 120000)
employee.get_info()
sm = employee.sum(2,56)
print(sm)
emp_str = "Mojidul-120000"
new_employee = Employee.from_string(emp_str)
new_employee.get_info()

