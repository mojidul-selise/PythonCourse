import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple argparse demonstration.")
# Add arguments
parser.add_argument("name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age", default=0)
# Parse the arguments
args = parser.parse_args()
# Use the arguments
print(f"Hello, {args.name}! You are {args.age} years old.")

#how to execute this file in command line
#Goto the localtion using cmd administrator and run the following command
#python argparse_command.py "Mojidul" --age 25