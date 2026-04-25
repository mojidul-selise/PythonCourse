student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A'}
print(student["name"])  # Output: Alice (accessing value by key)
print(student["age"])   # Output: 20 (accessing value by key)
print(student["grade"]) # Output: A (accessing value by key)

# Adding a new key-value pair to the dictionary
student["major"] = "Computer Science"
print(student)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A', 'major': 'Computer Science'}
# Modifying an existing value in the dictionary
student["age"] = 21
print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A', 'major': 'Computer Science'}
# Removing a key-value pair from the dictionary
del student["grade"]
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}
# Checking if a key exists in the dictionary
print("name" in student)  # Output: True (key "name" exists in the dictionary)
print("grade" in student)  # Output: False (key "grade" does not exist in the dictionary)
# Iterating through the dictionary keys and values
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 21
# major: Computer Science
# Getting the number of key-value pairs in the dictionary
print(len(student))  # Output: 3 (number of key-value pairs in the dictionary)
# Using the get method to access values
print(student.get("name"))  # Output: Alice (accessing value by key using get method)
print(student.get("grade", "Not Found"))  # Output: Not Found (key "grade" does not exist, returns default value "Not Found")

# Using the keys, values, and items methods to access dictionary components
print(student.keys())  # Output: dict_keys(['name', 'age', 'major'])
print(student.values())  # Output: dict_values(['Alice', 21, 'Computer Science'])
print(student.items())  # Output: dict_items([('name', 'Alice'), ('age', 21), ('major', 'Computer Science')])

#performance comparison between list and dictionary
import time
my_list = [i for i in range(1000000)]
my_dict = {i: i for i in range(1000000)}
# Measure time for list access
start_time = time.time()
for i in range(1000000):
    _ = my_list[i]
end_time = time.time()
print(f"List access time: {end_time - start_time}")

# Measure time for dictionary access
start_time = time.time()
for i in range(1000000):
    _ = my_dict[i]
end_time = time.time()
print(f"Dictionary access time: {end_time - start_time}")

# Dictionaries are generally faster than lists for lookups because they use a hash table to store key-value pairs, allowing for average-case O(1) time complexity for lookups, while lists have O(n) time complexity for lookups.
# Dictionaries are also more memory efficient than lists for large datasets because they only store unique keys, while lists can contain duplicate values. However, dictionaries may use more memory than lists for small datasets due to the overhead of storing key-value pairs and the hash table structure.

#dictionary pop method
student = { "name": "Alice", "age": 20, "grade": "A" }
age = student.pop("age")  # Removing the key "age" and returning its value
print(f"Removed age: {age}")  # Output: Removed age: 20
print(student)  # Output: {'name': 'Alice', 'grade': 'A'}
clear_result = student.clear()  # Removing all key-value pairs from the dictionary
print(clear_result)  # Output: None (the clear method does not return anything)