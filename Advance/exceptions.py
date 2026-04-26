while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  # Exit the loop if the operation is successful
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print(f"The result of {x} divided by {y} is: {z}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero second number.")
#executes if there is no exception
else:
    print("The division was successful.")

#raises an exception if the input is not a valid integer
def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
number = get_integer()
print(f"You entered: {number}")

#raises a custom exception
# if number < 10:
#     raise ValueError("This is a custom error message.") 

#finally block is executed regardless of whether an exception is raised or not
try:
    file = open("test_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("The file was opened successfully.")
    print(f"Content of the file:\n{content}")
finally:
    if 'file' in locals():
        file.close()
    print("This block is executed regardless of whether an exception is raised or not.")