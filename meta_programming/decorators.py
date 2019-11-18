# Decorator is way to add new functionality to existing function without modifying its original structure.


# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y
#
#
# def mul(x, y):
#     return x * y

# Now we need to print function name and parameter values when function get called.
# This should be applicable to all three function above. Like,
# def add(x, y):
#     print("add is called with parameter {0},{1}".format(x,y))
#     return x + y

# We can use decorators instead


def my_decorator(func):
	def wrapper_function(*args):
		print("{0} is called with parameter {1}".format(func.__name__, args))
		return func(*args)

	return wrapper_function


@my_decorator
def add(x, y):
	return x + y


@my_decorator
def sub(x, y):
	return x - y


@my_decorator
def mul(x, y):
	return x * y


add(5, 3)
sub(5, 3)
mul(5, 3)

# decorators are higher order function which takes function as argument and returns another function.

