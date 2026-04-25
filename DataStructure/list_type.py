numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adding an element to the end of the list
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)  # Inserting an element at a specific index
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6]
numbers.remove(3)  # Removing the first occurrence of an element
print(numbers)  # Output: [0, 1, 2, 4, 5, 6]
numbers.pop()  # Removing the last element
print(numbers)  # Output: [0, 1, 2, 4, 5]
numbers.pop(0)  # Removing an element at a specific index
print(numbers)  # Output: [1, 2, 4, 5]
numbers.clear()  # Removing all elements from the list
print(numbers)  # Output: []
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5 (number of elements in the list)
print(numbers[0])  # Output: 1 (first element)
print(numbers[-1])  # Output: 5 (last element)
numbers.reverse()  # Reversing the order of the list
print(numbers)  # Output: [5, 4, 3, 2, 1]
numbers.sort()  # Sorting the list in ascending order
print(numbers)  # Output: [1, 2, 3, 4, 5]
numbers.sort(reverse=True)  # Sorting the list in descending order
print(numbers)  # Output: [5, 4, 3, 2, 1]
numbers.sort(reverse=False)  # Sorting the list in ascending order
print(numbers)  # Output: [1, 2, 3, 4, 5]

#list comprehension
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5]