
fruits = "apple,banana,cherry"
fruit_list = fruits.split(",")  # This will split the string into a list of fruits
print(fruit_list)  # Output: ['apple', 'banana', 'cherry']

#joining a list of strings into a single string
joined_fruits = ", ".join(fruit_list)  # This will join the list of fruits into a single string with a comma and space as the separator
print(joined_fruits)  # Output: "apple, banana, cherry"