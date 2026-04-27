import os

current_directory = os.getcwd()
print("Current Directory:", current_directory)

#files = os.listdir(current_directory)
files = os.listdir(".") # "." represents the current directory
print("Files in the current directory:", files)

# Remove a file from the directory
try:
    os.remove("test1_file.txt")
except FileNotFoundError:
    print("File not found: test1_file.txt")
else:
    print("File 'test1_file.txt' removed successfully.")

print("Now try to read the file.")
try:
    file = open("test1_file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")

#create a new directory
new_directory = "test_directory"
try:
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created successfully.") 
except FileExistsError:
    print(f"Directory '{new_directory}' already exists.")
    
#remove the directory
try:
    os.rmdir(new_directory)
    print(f"Directory '{new_directory}' removed successfully.")
except FileNotFoundError:
    print(f"Directory '{new_directory}' not found.")
except OSError as e:
    print(f"Cannot remove directory: {e}")
    print(f"Directory '{new_directory}' is not empty. Remove files inside first.")
    
print("Now try to access the removed directory.")
try:
    os.listdir(new_directory)
except FileNotFoundError:
    print(f"Directory '{new_directory}' not found.")
    
#create a file in the new directory
os.makedirs(new_directory, exist_ok=True)
file_path = os.path.join(new_directory, "test1_file.txt")
try:
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("This is a test file inside the new directory.")
    print("File created successfully in the new directory.")
except OSError as e:
    print(f"Directory or file creation has error: {e}")

#rename the file inside the new directory
old_path = os.path.join(new_directory, "test1_file.txt")
new_path = os.path.join(new_directory, "test_file_rename.txt")
os.rename(old_path, new_path)

#check if the file is renamed
if os.path.exists(new_path):
    print("File renamed successfully.")
else:
    print("File rename failed.")
    
#join a path component in a platform-independent way
joined_path = os.path.join("new_directory", "subfolder", "test_file_rename.txt")
print("Joined Path:", joined_path)
