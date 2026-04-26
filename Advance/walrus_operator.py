#introduce in Python 3.8
#allows you to assign values to variables as part of an expression using the := operator

#without walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for number in numbers:
    squared = number ** 2
    squared_numbers.append(squared)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#with walrus operator
numbers = [1, 2, 3, 4, 5]
squared_numbers = [squared := number ** 2 for number in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#without walrus operator
with open("test_file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

#with walrus operator
with open("test_file.txt", "r") as f:
    while (line := f.readline()):
        print(line.strip())