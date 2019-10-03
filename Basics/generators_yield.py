# An iterator is an object adhering to the iterator protocol.
#   basically this means that it has a next method, which, when called, returns the next item in the sequence,
#   and when there is nothing to return, raises the StopIteration exception.

# Generator functions look and act just like regular functions, but with one defining characteristic.
# Generator functions use the Python yield keyword instead of return.
# generators are a great way to optimize memory.
# If the body of a def contains yield, the function automatically becomes a generator function.
# Reference: https://realpython.com/introduction-to-python-generators/#understanding-generators


def infinite_sequence():
	num = 0
	while True:
		# Return sends a specified value back to its caller whereas Yield can produce a sequence of values.
		# We should use yield when we want to iterate over a sequence, but do not want to store the entire sequence in memory.
		# Yield are used in Python generators.
		# A generator function is defined like a normal function, but whenever it needs to generate a value,
		#   it does so with the yield keyword rather than return.
		# Reference: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
		yield num
		num += 1

# Method1:
# for i in infinite_sequence():
# 	print("i: {}".format(i))
# Method2:
# seq = infinite_sequence()  # seq is a generator object
# while True:
# 	print("i: {}".format(next(seq)))


# When you call a generator function or use a generator expression, you return a special iterator called a generator.
# You can assign this generator to a variable in order to use it.
# When you call special methods on the generator, such as next(), the code within the function is executed up to yield.
# When the Python yield statement is hit, the program suspends function execution and returns the yielded value to
#   the caller. (In contrast, return stops function execution completely.)
# When a function is suspended, the state of that function is saved.
# This includes any variable bindings local to the generator, the instruction pointer, the internal stack,
#   and any exception handling.
# This allows you to resume function execution whenever you call one of the generator’s methods.



