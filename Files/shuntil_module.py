import shutil

# Create a directory to demonstrate shutil functions
shutil.os.makedirs("shutil_test_directory", exist_ok=True)
# Create a file in the new directory
file_path = shutil.os.path.join("shutil_test_directory", "test_file.txt")
with open(file_path, "w", encoding="utf-8") as file:
    file.write("This is a test file for shutil module demonstration.")
# Copy the file to a new location
shutil.copy(file_path, "shutil_test_directory/test_file_copy.txt")

# Move the copied file to a new location
shutil.move("shutil_test_directory/test_file_copy.txt", "shutil_test_directory/test_file_moved.txt")

#just copy a file in different file name
shutil.copy("shutil_test_directory/test_file.txt", "shutil_test_directory/test_file_copy2.txt")