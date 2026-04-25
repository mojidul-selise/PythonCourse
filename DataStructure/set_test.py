my_set = {"apple", "banana", "cherry"}
print(my_set)  # Output: {'apple', 'banana', 'cherry'}

my_set.add("orange")  # Adding an element to the set
print(my_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}
my_set.remove("banana")  # Removing an element from the set if not exist it will raise a KeyError
print(my_set)  # Output: {'apple', 'cherry', 'orange'}
my_set.discard("grape")  # Removing an element that does not exist (no error)
print(my_set)  # Output: {'apple', 'cherry', 'orange'}
my_set.pop()  # Removing an arbitrary element from the set(randomly removes an element)
print(my_set)  # Output: {'cherry', 'orange'} (the remaining elements may vary)
my_set.clear()  # Removing all elements from the set
print(my_set)  # Output: set()

#set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)  # Union of two sets
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
intersection_set = set_a.intersection(set_b)  # Intersection of two sets
print(intersection_set)  # Output: {3, 4}
difference_set = set_a.difference(set_b)  # Difference of two sets
print(difference_set)  # Output: {1, 2} uncommon elements in set_a
symmetric_difference_set = set_a.symmetric_difference(set_b)  # Symmetric difference of two sets
print(symmetric_difference_set)  # Output: {1, 2, 5, 6} uncommon elements in both sets

#checking subset and superset
set_c = {1, 2}
print(set_c.issubset(set_a))  # Output: True (set_c is a subset of set_a)
print(set_a.issuperset(set_c))  # Output: True (set_a is a superset of set_c)

#checking if an element is in a set
print(3 in set_a)  # Output: True (3 is an element of set_a)
print(5 in set_a)  # Output: False (5 is not an element of set_a)

#iterating through a set
for element in set_a:
    print(element)  # Output: 1 2 3 4 (the order may vary)

#sets are unordered collections of unique elements, so they do not maintain any specific order and do not allow duplicate values.
set_d = {1, 2, 2, 3, 4}
print(set_d)  # Output: {1, 2, 3, 4} (duplicate 2 is removed)

#sets can also be used to remove duplicates from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}
unique_list = list(unique_set)
print(unique_list)  # Output: [1, 2, 3, 4, 5] (the order may vary)