# Example2:
def multi_yield():
	yield_str = "This will print the first string"
	yield yield_str
	yield_str = "This will print the second string"
	yield yield_str


multi_obj = multi_yield()  # So a generator function returns an generator object that is iterable,
print(next(multi_obj))
print(next(multi_obj))
try:
	print(next(multi_obj))
except StopIteration as e:
	# As multi_yield method yielded two value, calling next on it for the third time will throw StopIteration error
	print("StopIteration")

# Applications: A normal function to return a sequence will create the entire sequence in memory before returning
#   the result. This is an overkill if the number of items in the sequence is very large.
# Generator implementation of such sequence is memory friendly and is preferred since it only produces one item
#   at a time.
# Generators are excellent medium to represent an infinite stream of data.
# Infinite streams cannot be stored in memory and since generators produce only one item at a time,
#   it can represent infinite stream of data.

