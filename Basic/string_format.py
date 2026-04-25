name = "Mojidul Islam"  # This is a string variable that stores the name "Mojidul Islam".
age = 25  # This is an integer variable that stores the age 25.

# Using string formatting to create a formatted string
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is Mojidul Islam and I am 25 years old."

#muline string formatting using f-strings (available in Python 3.6 and later)
formatted_string_f = f"My name is {name} and I am {age} years old."
print(formatted_string_f)  # Output: "My name is Mojidul Islam and I am 25 years old."

#muline string formatting using triple quotes
formatted_string_triple = """My name is {} and I am {} years old.""".format(name, age)
print(formatted_string_triple)  # Output: "My name is Mojidul Islam and I am 25 years old."

print("My name is {0} and I am {1} years old.".format("Mojidul Islam", 25))  # Output: "My name is Mojidul Islam and I am 25 years old."
print("My name is {name} and I am {age} years old.".format(name="Mojidul Islam", age=25))  # Output: "My name is Mojidul Islam and I am 25 years old." 

x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")  # Output: "The sum of 10 and 20 is 30."

pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")  # Output: "The value of pi is approximately 3.14."

#test alignment
print(f"{'Name':<10} {'Age':<5}")  # Output: "Name       Age  "
print(f"{name:<10} {age:<5}")  # Output: "Mojidul Islam 25   "
print(f"{'Name':>10} {'Age':>5}")  # Output: "      Name   Age"
print(f"{name:>10} {age:>5}")  # Output: "Mojidul Islam   25"  
print(f"{'Name':^10} {'Age':^5}")  # Output: "   Name    Age  "
print(f"{name:^10} {age:^5}")  # Output: "Mojidul Islam  25   "