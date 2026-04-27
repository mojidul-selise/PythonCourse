import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple argparse demonstration.")
parser.add_argument("filename", type=str, help="Name of the file to open")
# Parse the arguments
args = parser.parse_args()
# Try to open the file specified by the user
try:
    with open(args.filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{args.filename}' was not found.")
except Exception as e:
    print(f"Error: {e}")
    
#run from command line
#python arg_parse_file_open.py ../test_file.txt