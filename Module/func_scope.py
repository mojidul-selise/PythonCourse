#global scope = None
def func():
    #local scope = func
    x = 10
    print(x)

func()  # Output: 10
# print(x)  # This will raise a NameError because x is not defined in the global scope

#modify global variable
y = 5  # global variable
def modify_global():
    global y  # Declare that we want to modify the global variable y
    y = 10  # Modify the global variable
print(y)  # Output: 5 (before modification)
modify_global()
print(y)  # Output: 10 (after modification)

#documentation string
def add(a, b):
    """
    description:
    returns the sum of two numbers
    
    parameters:
    a (int): The first number
    b (int): The second number
    
    returns:
    int: The sum of two numbers
    """
    return a + b
result = add(3, 4)
print(result)  # Output: 7
print(add.__doc__)  # Output: "This function takes two numbers and returns their sum."
