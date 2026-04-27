import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
# Parse the arguments
args = parser.parse_args()
# Perform the calculation based on the operation
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    result = args.num1 / args.num2
else:
    result = "Invalid operation"

print(f"The result of {args.operation}ing {args.num1} and {args.num2} is {result}.")

#run from command line
#python arg_parse_calculator.py 2 3 multiply