#method overloading
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c = 0):#default parameter c
        return a+b+c
    
a = A()
print(a.add(2,3)) # Output: 5
print(a.add(2,3,4)) # Output: 9

print("Method overloading with default parameters:")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(3, 2)  # Default constructor
print(p1.x, p1.y)  # Output: 3 2
p2 = Point(5, 6)  # Default constructor with default values
print(p2.x, p2.y)  # Output: 5 6
#p = p1.sum(p2)  # Method overloading with default parameters
p = p1 + p2  # Using the __add__ method that is operator overloading
p.print_point()  # Output: X is 8 and Y is 8