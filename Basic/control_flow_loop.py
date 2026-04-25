#if statement
age = 20
if age >= 18:
    print("You are an adult.")
    
#if-else statement
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#if-elif-else statement
age = 20
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

#for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#while loop
count = 0
while count < 5:
    print(count)
    count += 1
    
#nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

#break statement
for i in range(10):
    if i == 5:
        break
    print(i)
    
#continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
#pass statement
for i in range(10):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)  # Print odd numbers
        
#else statement with loops
for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")
    
#nested loops with else statement
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
else:
    print("Nested loops completed successfully.")
    
#match-case statement (Python 3.10+)
command = "start"
match command:
    case "start":
        print("Starting the process.")
    case "stop":
        print("Stopping the process.")
    case "pause":
        print("Pausing the process.")
    case _:
        print("Unknown command.")