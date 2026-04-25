my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1 (first element)
print(my_tuple[-1])  # Output: 5 (last element)
# Tuples are immutable, so we cannot modify them
# my_tuple[0] = 10  # This will raise a TypeError
# However, we can concatenate tuples to create a new tuple
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)
# We can also unpack tuples into variables
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5
# We can use tuples to return multiple values from a function
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20

#counding occurrences of an element in a tuple
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
count_1 = my_tuple.count(1)
print(count_1)  # Output: 2 (number of occurrences of 1 in the tuple)
count_2 = my_tuple.count(2)
print(count_2)  # Output: 2 (number of occurrences of 2 in the tuple)
count_3 = my_tuple.count(3)
print(count_3)  # Output: 2 (number of occurrences of 3 in the tuple)

index_1 = my_tuple.index(1)
print(index_1)  # Output: 0 (index of the first occurrence of 1 in the tuple)
index_2 = my_tuple.index(2)
print(index_2)  # Output: 1 (index of the first occurrence of 2 in the tuple)

#tuples can also be used as keys in a dictionary
my_dict = {(1, 2): "a", (3, 4): "b"}
print(my_dict[(1, 2)])  # Output: "a" (value associated with the key (1, 2))
print(my_dict[(3, 4)])  # Output: "b" (value associated with the key (3, 4))

#tuple is faster than list for iteration and access because of its immutability
import time

# Example of performance comparison
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# Measure time for list access
start_time = time.time()
for _ in range(1000000):
    _ = my_list[2]
end_time = time.time()
print(f"List access time: {end_time - start_time}")

# Measure time for tuple access
start_time = time.time()
for _ in range(1000000):
    _ = my_tuple[2]
end_time = time.time()
print(f"Tuple access time: {end_time - start_time}")