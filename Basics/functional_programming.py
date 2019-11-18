# Python provides features like lambda, filter, map, and reduce that can easily demonstrate
#   the concept of Functional Programming.
# Reference: https://towardsdatascience.com/elements-of-functional-programming-in-python-1b295ea5bbe0
from functools import reduce

# Lambda expressions - also known as 'anonymous functions' - allow us to create and use a function in a single line.
func = lambda x: 5*x+2  # This lambda function will take the input x and return 5x + 2
# Here lambda keyword is used to create an anonymous fucntion which we are using by func
print("func: {}".format(func(3)))

func1 = lambda : "I am an anonymous function"
func2 = lambda x: 5*x+2
func3 = lambda x, y: x+y
func4 = lambda x, y, z: (x+y+z, x-y-z)

print("func1: {}".format(func1()))
print("func2: {}".format(func2(3)))
print("func3: {}".format(func3(3, 2)))
print("func4: {}".format(func4(6, 2, 3)))

# let's look at a common use of Lambda function where we do not assign it a name.
# Let's say we have a list of the first seven U.S Presidents and we'd like to sort this list by their last name.
# We shall create a Lambda function that extracts the last name, and uses that as the sorting value.
presidents_usa = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", 
                  "John Quincy Adams", "Andrew Jackson"]
presidents_usa.sort(key=lambda name: name.split(" ")[-1].lower())
print("presidents_usa: {}".format(presidents_usa))


# The map function
# The map function applies a function to every item of iterable, yielding the results.
# When used with lists, Map transforms a given list into a new list by applying the function
#   to all the items in an input_list.
# Syntax: map(function_to_apply, iterables)
volume = lambda x: x*x*x
print("Find volume of edges [1, 2, 3]: {}".format(list(map(volume, [1, 2, 3]))))
# output of the map function is not a list but a map object,
#   which is an iterator over the results. We can, however, turn this into a list
#   by passing the map to the list constructor.


# The Filter Function
# The 'filter' function constructs an iterator from those elements of iterable for which function returns true.
# Syntax: filter(function, iterable)
my_list = [5, 7, 2, 10, 9, 2, 3, 6]
output_list = filter(lambda x: x > 5, my_list)
print("output_list: {}".format(list(output_list)))

countries_asia = ['Afg', '', 'Bhutan', '', 'China', '', '', 'India']
print("Filter blank countries: {}".format(list(filter(None, countries_asia))))
# This filters out all values that are treated as false in a boolean setting.


# The Reduce Function
# The 'reduce' function transforms a given list into a single value by applying a
#   function cumulatively to the items of sequence, from left to right,
# Syntax: reduce(function, seq)
product = reduce(lambda x, y:x*y, [1, 2, 3, 4, 5])
print("product: {}".format(product))


# List Comprehensions: Alternative to map, filter and reduce
# List comprehension is a way to define and create lists in Python.
# In most cases, list comprehensions let us create lists in a single line of code
#   without worrying about initializing lists or setting up loops.
squares = [x**2 for x in range(10)]
print('squares: {}'.format(squares))


# List Comprehensions vs. Map function
height_width = [(1, 2), (4, 5), (6, 7)]
area = [height*width for (height, width) in height_width]
print("area: {}".format(area))


# List Comprehensions vs. Filter function
print("List Comprehensions vs. Filter function: {}".format([country for country in countries_asia if country != '']))


# List Comprehensions vs. Reduce function
print("List Comprehensions vs. Reduce function: {}".format([x for x in my_list if x > 5]))
