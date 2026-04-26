#positional arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)  # Output: Hello Alice, you are 30 years old.
greet("Bob", 25)    # Output: Hello Bob, you are 25 years old.

#keyword arguments
greet(name="Charlie", age=35)  # Output: Hello Charlie, you are 35 years old.
greet(age=28, name="David")    # Output: Hello David, you are 28 years old.

#example of positional
def my_function(*args):
    print(type(args))  # Output: <class 'tuple'>
    for arg in args:
        print(arg)
        
my_function(1, 2, 3, "Hello")  # Output: 1 2 3 Hello

#example of keyword arguments
def my_function(**kwargs):
    print(type(kwargs))  # Output: <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
my_function(name="Mojidul", age=30, city="Dhaka", country="Bangladesh")