#map function is used to apply a function to all the items in an iterable (list, tuple etc.) and return a map object (an iterator)
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x**2

squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


#discuss lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#filter function is used to filter the elements of a sequence based on a function that returns a boolean value
numbers = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

#combine map and filter
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(squared_even_numbers)  # Output: [4, 16]

#None values are filtered out by filter function
numbers = [1, 2, [], "", "Mojidul", 4, None]
filtered_numbers = list(filter(None, numbers))
print(filtered_numbers)  # Output: [1, 2, "Mojidul", 4]

#reduce function#reduce function is used to apply a function of two arguments cumulatively to the items of a sequence from left to right, reducing the sequence to a single value
#ruduce is not a built-in function, it is part of the functools module
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)  # Output: 15

#using lambda function with reduce
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

