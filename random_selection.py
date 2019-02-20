import random

mylist = ['can', 'be', 'changed']
mytuple = ('cannot', 'be', 'changed')
mydict = {'name': 'dipal', 'lastname': 'modi'}

# choice() returns a random item from a list, tuple, or string.
print('Choice: ', random.choice(mylist))

# The method randrange() returns a randomly selected element from range(start, stop, step).
# Select an even number in 100 <= number < 1000
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))

# The method random() returns a random float r, such that 0 is less than or equal to r and r is less than 1.
print('random between 0 and 1: ', random.random())

# The method uniform() returns a random float r, such that x is less than or equal to r and r is less than y.
print("latitude: " + str(uniform(-180, 180)))
print("longitude: " + str(uniform(-90, 90)))
