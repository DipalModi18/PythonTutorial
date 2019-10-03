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


# Variable-length Arguments
def printinfo2(*vartuple):
    for var in vartuple:
        print(var)
    return


printinfo2()
printinfo2(70, 60, 50)

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
