# try:
#     with open('test_file.txt', 'r') as file:
#         content = file.read()
#         print(content)
#         file.close()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Finished attempting to read the file.")
    
#if file is not found, it will automatically create a new file and write to it 
try:
    with open('test1_file.txt', 'w') as file:
        file.write("This is a test file.\nIt contains multiple lines of text.")
    print("File written successfully.")
    file.close()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Finished attempting to write to the file.")

#Another way to read a file line by line    
try:
    file = open('test1_file.txt', 'r')
    for line in file:
        print(line.strip()) #strip() is used to remove any leading or trailing whitespace characters from the line
    file.close()
except FileNotFoundError:
    print("File not found.")
    
#appending to a file
try:
    with open('test1_file.txt', 'a') as file:
        file.write("\nThis line is appended to the file.")
    print("Line appended successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\nReading the file after appending:")   
try:
    file = open('test1_file.txt', 'r')
    for line in file:
        print(line.strip()) #strip() is used to remove any leading or trailing whitespace characters from the line
    file.close()
except FileNotFoundError:
    print("File not found.")
    
  