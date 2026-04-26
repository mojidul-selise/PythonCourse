def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

#one way to use the decorator
def greeting():
    print("Hello Python!")
message = my_decorator(greeting)
message()

#another way to use the decorator with syntactic sugar
@my_decorator
def say_hello():
    print("Hello, World!")
    
say_hello()

#decorator with parameters
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Mojidul")  # Output: Hello, Mojidul! (repeated 3 times)

#chaining multiple decorator
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def add_exclamation(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@uppercase
@add_exclamation
def greting():
    return "Hello"

print(greting())