# Function with required arguments
def myfunc(str):
    """function doc_string"""
    return str[2:]


print('calling function: ', myfunc('hello'))


# Function with keyword arguments -
# This allows you to skip arguments or place them out of order because the Python interpreter is able to use the
#                       keywords provided to match the values with parameters.
def myfunc2(str, num):
    print('str: ', str, 'num: ', num)


myfunc2(num=2, str='string')


# default arguments
def printinfo(name, age=21):
    """This prints a passed info into this function"""
    print("Name: ", name)
    print("Age ", age)
    return


printinfo('dipal')
printinfo('dipal', 22)


# Variable-length Arguments --
# 1. args
# 2. kwargs
# Reference: https://www.geeksforgeeks.org/args-kwargs-python/

# 1. The special syntax *args in function definitions in python is used to pass a variable
#   number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
def printinfo2(*args):
    for var in args:
        print(var)
    return


printinfo2()
printinfo2(70, 60, 50)


def printinfo3(first_arg, *args):
    print("First argument: {}".format(first_arg))
    for arg in args:
        print("Next arg: {}".format(arg))


printinfo3(3, 4, 5)
printinfo3("aa")


# The special syntax **kwargs in function definitions in python is used to pass a keyworded,
#   variable-length argument list. We use the name kwargs with the double star.
#   The reason is because the double star allows us to pass through keyword arguments (and any number of them).
def printinfo4(**kwargs):
    for key, value in kwargs.items():
        print("Key: {} Value: {}".format(key, value))


printinfo4(greeting="Hi", name="Dipal")
printinfo4(num=1, func="add")


# The Anonymous Functions
# These functions are called anonymous because they are not declared in the standard manner by using the def keyword.
#                       You can use the lambda keyword to create small anonymous functions.
# Lambda forms can take any number of arguments but return just one value in the form of an expression.
#                       They cannot contain commands or multiple expressions.
# An anonymous function cannot be a direct call to print because lambda requires an expression.
# Lambda functions have their own local namespace and cannot access variables other than those in their parameter list
#                       and those in the global namespace.
# Although it appears that lambdas are a one-line version of a function,
#                       they are not equivalent to inline statements in C or C++,
#                       whose purpose is to stack allocation by passing function,
#                       during invocation for performance reasons.
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total : ", sum(20, 20))


# Inner functions - Functions are also allowed to be defined inside a function as shown in the code below
def print_greeting(greeting, uppercase):

    def print_text_lowercase(text):
        print(text.lower())

    def print_text_uppercase(text):
        print(text.upper())
    if uppercase:
        print_text_uppercase(text=greeting)
    else:
        print_text_lowercase(text=greeting)


print_greeting(greeting='hI', uppercase=True)
print_greeting(greeting="hI", uppercase=False)


# Functions can be
# 1.They can be passed as arguments to other functions,
# 2. returned as values from other functions, and
# 3. assigned to variables and stored in data structures.

# 1. Functions in python are treated as first-class objects. Therefore functions can be passed as
#   arguments to another function just like strings, integers, or any other object.
def print_hi():
    print("hi")


def run_any_function(function):
    function()


run_any_function(function=print_hi)


# 2. Functions can also be returned from a function as the output:
# Reference: https://levelup.gitconnected.com/handy-python-features-e33751ef98a8
def get_capable_function(uppercase):
    def print_lowercase(text):
        print(text.lower())

    def print_uppercase(text):
        print(text.upper())

    if uppercase:
        return print_uppercase
    else:
        return print_lowercase


get_capable_function(uppercase=True)("hI")
get_capable_function(uppercase=False)("Hi")


# 3.
def myFunc(a, b):
    return a + b


functions = [myFunc]  # 3.
print("type(functions[0]): {}".format(type(functions[0])))
print("functions[0](2, 3): {}".format(functions[0](2, 3)))


# Decorators are functions that wrap a function and change their behavior.
#   These functions take a function as an argument. They have an inner function defined
#   which can invoke the function taken as the argument changing its behavior.
def print_hi_and_name(name_only_function):
    def add_hi():
        print("Hi ")
        name_only_function()
    return add_hi


def print_name():
    print("Dipal")


print_name = print_hi_and_name(print_name)
print_name()


# There is a more concise and short way to achieve the same result instead of re-declaring the function
def print_hi_and_name_2(name_only_function):
    def add_hi():
        print("Hi")
        name_only_function()
    return add_hi


@print_hi_and_name
def print_name():
    print("Dipal")


print_name()


# The function print_name() prints a hard-coded value.
#   Suppose we need to pass a name as an argument into that function and the new function
#   becomes print_name(name) now. But the inner function which invokes this does not know the
#   arguments required by the function. It should also be changed accordingly which would give an error otherwise:
def print_hi_and_name(name_only_function):
    def add_hi(name):
        print("Hi")
        name_only_function(name)
    return add_hi


@print_hi_and_name
def print_name(name):
    print(name)


print_name("Dipal")
