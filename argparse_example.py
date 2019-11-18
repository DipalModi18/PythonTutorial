import argparse
import os
# argparse - parse the arguments.

parser = argparse.ArgumentParser(description="Argument parser")

# positional arguments
parser.add_argument("var1", type=str, help="Provide value for var1")
parser.add_argument("var2", type=str, help="Provide value for var2")
# var1 and var2 are positional arguments. They are mandatory to be passed in the required position.
# Running python3 argparse_example.py will output the following error
# argparse_example.py: error: the following arguments are required: var1, var2

# optional arguments
# Optional arguments are created just like positional arguments except that they have a '--' double dash
#   at the start of their name (or a'-' single dash and one additional character for the short version).
#   For example, you can create an optional argument with parser.add_argument('-m', '--my_optional').
parser.add_argument("--var3", default=2, help="Provide value for var3 (default: 2)")
parser.add_argument("--var4", default=os.getenv("Var4", "var4 value"), help="Provide value for var4")

args = parser.parse_args()
print(" ".join([args.var1, args.var2]))  # Run using: python3 argparse_example.py "hello" "world"
# For help: python3 argparse_example.py -h or python3 argparse_example.py --help
print(args.var3)
# python3 argparse_example.py "hello" "world" --var3=3
print(args.var4)
#  python3 argparse_example.py "hello" "world"  --> Var4 not in the env so returns default value
# export Var4="any value"
# Run the argparse_example.py again
